let mymap = L.map("map", {
    center: [30, -66],
    zoom:4
});

//
function getColorByWindSpeed(windSpeed) {
    if (windSpeed < 74) return '#33cc33'; // Tropical Depression (Green)
    else if (windSpeed < 96) return '#ffcc00'; // Tropical Storm (Yellow)
    else if (windSpeed < 111) return '#ff9900'; // Category 1 Hurricane (Light Orange)
    else if (windSpeed < 130) return '#ff6600'; // Category 2 Hurricane (Orange)
    else if (windSpeed < 157) return '#ff3300'; // Category 3 Hurricane (Red-Orange)
    else if (windSpeed < 178) return '#cc0000'; // Category 4 Hurricane (Red)
    else return '#990000'; // Category 5 Hurricane (Dark Red)
}

//Add tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(mymap);

  d3.csv("http://localhost:8000/hurricanes.csv").then(function (data) {
    let groupedData = {};
    let maxWindSpeedByHurricane = {};

    data.forEach(function (row) {
        const latitude = parseFloat(row.lat);
        const longitude = parseFloat(row.long);
        const hurricaneName = row.name;
        const windSpeed = parseFloat(row.wind);

        console.log(`[${latitude}, ${longitude}]`)


        // Only process data for the specified hurricane
        if (hurricaneName === 'Ivan') { 
            if (!groupedData[hurricaneName]) {
                groupedData[hurricaneName] = [];
                maxWindSpeedByHurricane[hurricaneName] = windSpeed;
            } else {
                maxWindSpeedByHurricane[hurricaneName] = Math.max(maxWindSpeedByHurricane[hurricaneName], windSpeed);
            }

        // // For mapping ALL hurricanes
        // if (!groupedData[hurricaneName]) {
        //     groupedData[hurricaneName] = [];
        //     maxWindSpeedByHurricane[hurricaneName] = windSpeed;
        // } else {
        //     maxWindSpeedByHurricane[hurricaneName] = Math.max(maxWindSpeedByHurricane[hurricaneName], windSpeed);
        // }

        groupedData[hurricaneName].push([latitude, longitude]);
        console.log("=============")
        console.log(groupedData)
        }

        // Create a marker for each data point
        // L.marker([latitude, longitude])
        //     .addTo(mymap)
        //     .bindPopup(`<b>${row.name}</b><br>Status: ${row.status}<br>Wind: ${row.wind}<br>Pressure: ${row.pressure}`);
    });

    for (let hurricaneName in groupedData) {
        let polyline = L.polyline(groupedData[hurricaneName], {
            color: getColorByWindSpeed(maxWindSpeedByHurricane[hurricaneName]),
            weight: 3,
        }).addTo(mymap).bindPopup(`<b>${hurricaneName}</b>`);
    }
});

//magnitude of marker to be wind speed and connect markers for each hurricane/color code