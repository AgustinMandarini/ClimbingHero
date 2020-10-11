var mapboxUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw'
var mapboxAttribution = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'

var satellite = L.tileLayer(mapboxUrl, {id: 'mapbox/satellite-v9', maxZoom: 18, tileSize: 512, zoomOffset: -1, attribution: mapboxAttribution}),
    urban     = L.tileLayer(mapboxUrl, {id: 'mapbox/streets-v11', maxZoom: 18, tileSize: 512, zoomOffset: -1, attribution: mapboxAttribution});

var map = L.map('map', {
    center: [-33.625215, -69.515620],
    zoom: 13,
    layers: [satellite, urban]
  });

var baseMaps = {
    "Satellite": satellite,
    "Urban": urban
};
L.control.layers(baseMaps).addTo(map);

//Sector areas recieved from /home route
//featureGroup variable is recieved in map.html template
L.geoJSON(featureGroup).addTo(map);
