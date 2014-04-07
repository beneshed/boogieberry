/* Add Your Company Name latitude and  longitude here.
 * for latitude and longitude please check http://itouchmap.com/latlong.html
 *  */
	var latitude_1 = "41.253032";
	var longitude_1 = "-72.520752";
	var details_1 = "Company Name - Brooklyn, NY, United States";
	
	var latitude_2 = "42.253032";
	var longitude_2 = "-73.520752";
	var details_2 = "Company Name - Reliance, NY, United States";
	
	function LoadGmaps_basic() {
		var myLatlng = new google.maps.LatLng(latitude_1, longitude_1);
		var myOptions = {
			zoom : 8,
			scrollwheel : true,
			center : myLatlng,
			navigationControl : true,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		}
	
		var map = new google.maps.Map(document.getElementById("googlemaps"), myOptions);
		var marker = new google.maps.Marker({
			position : myLatlng,
			map : map,
			icon : 'img/map_icon.png'
		});
		var infowindow = new google.maps.InfoWindow({
			content : details_1
		});
		google.maps.event.addListener(marker, "click", function() {
			infowindow.open(map, marker);
	
		});
	
	}
	
	function LoadGmaps_markers() {
		var myLatlng_1 = new google.maps.LatLng(latitude_1, longitude_1);
		var myLatlng_2 = new google.maps.LatLng(latitude_2, longitude_2);
		var myOptions = {
			zoom : 6,
			scrollwheel : true,
			center : myLatlng_1,
			navigationControl : true,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		}
	
		var map = new google.maps.Map(document.getElementById("googlemaps_markers"), myOptions);
		var marker_1 = new google.maps.Marker({
			position : myLatlng_1,
			map : map,
			icon : 'img/map_icon.png'
		});
		var marker_2 = new google.maps.Marker({
			position : myLatlng_2,
			map : map,
			icon : 'img/map_icon.png'
		});
		var infowindow_1 = new google.maps.InfoWindow({
			content : details_1
		});
		var infowindow_2 = new google.maps.InfoWindow({
			content : details_2
		});
		google.maps.event.addListener(marker_1, "click", function() {
			infowindow_1.open(map, marker_1);
		});
		google.maps.event.addListener(marker_2, "click", function() {
			infowindow_2.open(map, marker_2);
		});
	
	}
	
	
	function initialize() {
				  var map = new google.maps.Map(document.getElementById('map-canvas'), {
				    mapTypeId: google.maps.MapTypeId.ROADMAP
				  });
				  var defaultBounds = new google.maps.LatLngBounds(
				      new google.maps.LatLng(-33.8902, 151.1759),
				      new google.maps.LatLng(-33.8474, 151.2631));
				  map.fitBounds(defaultBounds);
				
				  var input = /** @type {HTMLInputElement} */(document.getElementById('target'));
				  var searchBox = new google.maps.places.SearchBox(input);
				  var markers = [];
				
				  google.maps.event.addListener(searchBox, 'places_changed', function() {
				    var places = searchBox.getPlaces();
				
				    for (var i = 0, marker; marker = markers[i]; i++) {
				      marker.setMap(null);
				    }
				
				    markers = [];
				    var bounds = new google.maps.LatLngBounds();
				    for (var i = 0, place; place = places[i]; i++) {
				      var image = {
				        url: place.icon,
				        size: new google.maps.Size(71, 71),
				        origin: new google.maps.Point(0, 0),
				        anchor: new google.maps.Point(17, 34),
				        scaledSize: new google.maps.Size(25, 25)
				      };
				
				      var marker = new google.maps.Marker({
				        map: map,
				        icon: image,
				        title: place.name,
				        position: place.geometry.location
				      });
				
				      markers.push(marker);
				
				      bounds.extend(place.geometry.location);
				    }
				
				    map.fitBounds(bounds);
				  });
				
				  google.maps.event.addListener(map, 'bounds_changed', function() {
				    var bounds = map.getBounds();
				    searchBox.setBounds(bounds);
				  });
				}
				
				google.maps.event.addDomListener(window, 'load', initialize);
	
	/* for Google map init */
				$(window).load(function() {
					LoadGmaps_basic();
					LoadGmaps_markers(); 
				});
    