# -*- coding: utf-8 -*-
#import urllib2
import requests
import json
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
			topArtists = Top3Artists(request.POST['favorite_artist'])
			return render(request, 'form/submitted.html', {'form': request.POST, 'artists': topArtists})
    else:
        form = NameForm()
    return render(request, 'form/form.html', {'form': form})

class NameForm(forms.Form):
    fullname = forms.CharField(label='Fullständigt namn', max_length=100)
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Gatuadress")
    zipcode = forms.DecimalField(label="Postnummer")
    city = forms.CharField(label="Ort")
    favorite_artist = forms.CharField(label="Din favorit artist")

def Top3Artists(artist):
	topArtists = requests.get("http://ws.audioscrobbler.com/2.0/", params={"method": "artist.gettoptracks", "artist": artist, "api_key": "ec96cbbaf5fd427e09d06c6c63ce31be", "format":"json"}).json()
	return topArtists