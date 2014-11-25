$(document).ready(function(){
	var validate = $('.validate')
	validate.submit( function (e){
		e.preventDefault();
    	$(".errorlist").remove();
		if(validateForm()){
			validate[0].submit();
		}
	});
	function validateForm() {
	    var error_occured = false;

	    var fullname = $("#id_fullname");
	    var email = $("#id_email");
	    var address = $("#id_address");
	    var zipcode = $("#id_zipcode");
	    var city = $("#id_city");
	    var favorite_artist = $("#id_favorite_artist");
	    //Validate fullname
	    if (fullname.val() == null || fullname.val() == "") {
	    	fullname.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	        error_occured = true;
	    }

	    //Validate email
	    emailval = email.val();
	    if(emailval == null || emailval == ""){
	    	email.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	    	error_occured = true;
	    }

    	//Validate address
	    if (address.val() == null || address.val() == "") {
	    	address.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	        error_occured = true;
	    }

    	//Validate zipcode
    	var ex = /^\d{5}$/;
    	var re = new RegExp(re);
	    if (zipcode.val() == null || zipcode.val() == "") {
	    	zipcode.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	        error_occured = true;
	    }
	    else if(!/^\d{5}$/.test(zipcode.val())){
    		zipcode.parent().before('<ul class="errorlist"><li>Måste vara 5 siffror</li></ul>');
	        error_occured = true;
	    }

	    //Validate city
	    if (city.val() == null || city.val() == "") {
	    	city.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	        error_occured = true;
	    }

	    //Validate favorite artist
	    if (favorite_artist.val() == null || favorite_artist.val() == "") {
	    	favorite_artist.parent().before('<ul class="errorlist"><li>Detta fält måste fyllas i.</li></ul>');
	        error_occured = true;
	    }
	    if(!error_occured){
	    	return true;
	    }
	}
});