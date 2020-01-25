function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
    	localStorage.setItem('_loc', 'NA')
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
	var lat = position.coords.latitude;
	var lng = position.coords.longitude;
	
	console.log(lat, lng);

	alert(lat + ',' + lng);

	localStorage.setItem('_loc', lat + ',' + lng)
}

function showLoc(){
	alert(localStorage.getItem('_loc'));
}