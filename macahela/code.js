let mymap = L.map("map", {
    center: [25.7617, -80.1918],
    zoom:4
});

//Add tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(mymap);

d3.csv("http://localhost:8000/hurricanes.csv").then(function (data) {
    // Iterate through the CSV data and create markers
    data.forEach(function (row) {
        const latitude = parseFloat(row.lat);
        const longitude = parseFloat(row.long);

        // Create a marker for each data point
        L.marker([latitude, longitude])
            .addTo(mymap)
            .bindPopup(`<b>${row.name}</b><br>Status: ${row.status}<br>Wind: ${row.wind}<br>Pressure: ${row.pressure}`);
    });
});

//magnitude of marker to be wind speed and connect markers for each hurricane/color code