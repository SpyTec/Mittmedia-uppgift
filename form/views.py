# -*- coding: utf-8 -*-
import requests
import json
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect

def index(request):
	# Om formuläret skickas
    if request.method == 'POST':
        form = NameForm(request.POST)
        # Är formuläret giltig? Kollar även CSRF nyckeln
        if form.is_valid():
        	# Ta fram topArtisterna - Visar upp top 3 i form/submitted.html
			topArtists = TopArtists(request.POST['favorite_artist'])
			# Rendera html fil
			return render(request, 'form/submitted.html', {'form': request.POST, 'artists': topArtists})
	# Om formulär inte skickas
    else:
        form = NameForm()
    # Rendera html fil
    return render(request, 'form/form.html', {'form': form})

class NameForm(forms.Form):
	# Lägg till validerings checkar, namn samt etiketter
    fullname = forms.CharField(label='Fullständigt namn', max_length=100)
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Gatuadress")
    zipcode = forms.DecimalField(label="Postnummer")
    city = forms.CharField(label="Ort")
    favorite_artist = forms.CharField(label="Din favorit artist")

def TopArtists(artist):
	# Genom requests modulen ta fram top låtar från variablen 'artist'
	topArtists = requests.get("http://ws.audioscrobbler.com/2.0/", params={"method": "artist.gettoptracks", "artist": artist, "api_key": "ec96cbbaf5fd427e09d06c6c63ce31be", "format":"json"})
	return topArtists.json()
