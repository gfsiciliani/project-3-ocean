document.addEventListener('DOMContentLoaded', function () {
    // Fetch initial data and update graph for the default location
    fetchAndPlotData('Abaco');

    // Add event listener to the dropdown
    document.getElementById('locationDropdown').addEventListener('change', updateGraphByLocation);
});

// Function to fetch data and update graph
function fetchAndPlotData(location) {
    d3.json(`http://localhost:5000/api/data/${location}`).then(
        (data) => {
            // Store the initial data in a global variable based on location
            window[`${location}Data`] = data;

            // Update the graph with the initial data
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

// Function to update the graph based on the selected location from the dropdown
function updateGraphByLocation() {
    // Get selected location from the dropdown
    var selectedLocation = document.getElementById('locationDropdown').value;

    // Update the graph for the selected location
    fetchAndPlotData(selectedLocation);
}
