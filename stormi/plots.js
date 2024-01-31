// Fetch data and update graph on page load
document.addEventListener('DOMContentLoaded', function () {
    // Fetch initial data and update graph
    fetchAndPlotData();
});

// Function to fetch data and update graph
function fetchAndPlotData() {
    d3.json('http://localhost:5000/api/data').then(
        (data) => {
            // Store the initial data in a global variable
            window.allData = data;

            // Create the dropdown options based on unique years in the data
            createDropdownOptions();

            // Update the graph with the initial data
            updateGraph();
        }
    );
}

// Function to create dropdown options based on unique years
function createDropdownOptions() {
    var years = getUniqueYears(allData);

    // Get the dropdown element
    var dropdown = document.getElementById('yearDropdown');

    // Clear existing options
    dropdown.innerHTML = '';

    // Add default option
    var defaultOption = document.createElement('option');
    defaultOption.text = 'Select Year';
    defaultOption.value = '';  // You can set a default value if needed
    dropdown.add(defaultOption);

    // Add options for each year
    years.forEach(function (year) {
        var option = document.createElement('option');
        option.text = year;
        option.value = year;
        dropdown.add(option);
    });
}

// Function to get unique years from the data
function getUniqueYears(data) {
    var uniqueYears = new Set();
    data.forEach(function (item) {
        var year = item.time.split('-')[0];  // Assuming 'time' is in the format 'YYYY-MM-DD HH:mm:ss'
        uniqueYears.add(year);
    });
    return Array.from(uniqueYears);
}

// Function to update the graph based on the selected year
function updateGraph() {
    // Get selected year from the dropdown
    var selectedYear = document.getElementById('yearDropdown').value;

    // Filter data for the selected year
    var filteredData = getDataForYear(selectedYear);

    // Update the graph with the filtered data
    updateGraphWithData(filteredData);
}

// Function to filter data based on the selected year
function getDataForYear(year) {
    return allData.filter(item => item.time.startsWith(year));
}

// Function to update the graph with the provided data
function updateGraphWithData(filteredData) {
    let time = [];
    let airTemp = [];

    for (let i = 0; i < filteredData.length; i++) {
        time.push(filteredData[i].time);
        airTemp.push(filteredData[i].air_temperature_noaa);
    }

    let graphTitle = 'Your Graph Title';

    let trace1 = {
        x: time,
        y: airTemp,
        name: 'Your Graph Name',
        type: 'line'
    };

    let layout = {
        title: graphTitle
    };

    Plotly.newPlot('plot', [trace1], layout);
}
