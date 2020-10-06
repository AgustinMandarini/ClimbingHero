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

var popuptag = "<b>Sector name</b><br>Routes"
var featureGroup = L.featureGroup().bindPopup(popuptag).addTo(map);
var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: featureGroup
          }
}).addTo(map);

map.on('draw:created', function(e) {
   // Each time a feaute is created, it's added to the over arching feature group
   featureGroup.addLayer(e.layer);
});

// on click, clear all layers
document.getElementById('delete').onclick = function(e) {
    featureGroup.clearLayers();
}

var data;
document.getElementById('export').onclick = function(e) {
    // Extract GeoJson from featureGroup
    data = featureGroup.toGeoJSON();

    // Stringify the GeoJson
    var convertedData = 'text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data));

    // Create export
    document.getElementById('export').setAttribute('href', 'data:' + convertedData);
    document.getElementById('export').setAttribute('download','data.geojson');
}
