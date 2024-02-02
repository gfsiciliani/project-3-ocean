
document.getElementById('selDataset').addEventListener('change', optionChanged);
let selectedId = document.getElementById('selDataset').value;

d3.json(url).then(response => {
    let samples = response.samples;
    let name = response.samples.find(item => item.id === selectedId);
    let otuIds = name.otu_ids;
    let sampleValues = name.sample_values;
    let otuLabels = name.otu_labels;

    let barData = [{
        x: sampleValues.slice(0, 10).reverse(),
        y: otuIds.map(id => `OTU ${id}`).slice(0, 10).reverse(),
        type: 'bar',
        orientation: 'h'
    }];

    let barLayout = {
        autosize: true,};

Plotly.newPlot('bar', barData, barLayout);
});


function populateDropdown(names) {
    for (let i = 0; i < names.length; i++) {
        let option = document.createElement('option');
        option.text = names[i];
        document.getElementById('selDataset').add(option);
    }
};


d3.json(url).then(response => {
    let samples = response.samples;
    let names = samples.map(item => item.id);
    populateDropdown(names);
});


document.getElementById('selDataset').removeEventListener('change', optionChanged);