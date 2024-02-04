document.addEventListener('DOMContentLoaded', function () {

    fetchAndPlotData('Abaco');

    document.getElementById('locationDropdown').addEventListener('change', updateGraphByLocation);
});

// Function to fetch data and update graph
function fetchAndPlotData(location) {
    d3.json(`http://localhost:5000/api/data/${location}`).then(
        (data) => {
            
            window[`${location}Data`] = data;

          
            updateGraph(data, location);
        }
    );
}

// Function to update the graph based on the selected location
function updateGraph(data, location) {
    console.log('Graph Data:', data);

    let traces = Array.from({ length: 3 }, (_, i) => {
        let year = 2018 + i;
        return {
            x: data.map(entry => entry.time),
            y: data
                .filter(entry => entry.time.startsWith(year))
                .map(entry => entry.air_temperature_noaa),
            name: year.toString(),
            type: 'line'
        };
    });

    let layout = {
        title: `Air Temperature for ${location}`
    };

    Plotly.newPlot('plot', traces, layout);
}


function updateGraphByLocation() {

    var selectedLocation = document.getElementById('locationDropdown').value;

    fetchAndPlotData(selectedLocation);
}
