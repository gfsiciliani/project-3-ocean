# Project 3 - Data Visualization, Weather

## Overview
Our project presents an analytical journey through selected facets of global climate change, focusing CO2 emissions, hurricane activities, and global temperature trends.

## Instructions
Webpage contains three sets of visuals, two of which are interractive. One showing the paths of category 5 hurricanes, their routes clickable to reveal their name, and datapoints clickable to reveal the windspeed. The second visual may be interracted with via a drop-down menu which selects a geographic location for the graph to compare three years of temperature data.

## Ethical Considerations
While all trends do show a positive correlation between climate change and the increase in storms and their wind speeds, some scientists (DOI: https://doi.org/10.1175/2009JCLI3034.1) do emphasize that context is crucial, and increased scientific abilites now allow us to be aware of storms that are more short lived, especially short storms that never reach land. They also claim that for optimal scientific studies, they would look at more than 100 years of data, which is difficult due to technological gaps in the past.

We also understand that our data is only looking at Atlantic storms. This ignores a significant part of the world that also experiences tropical cyclones, and our exclusion of them from this study is a gap in our analysis. While that data may be available online, we chose to stay with largely United States research studies (with the exception of Argo/Argovis data used) which is a notably lack in data diversity.

Lastly, we did have considerable personal bias going into this project. While we beleive that our findings back up our biases and maintain scientific integrity (climate change is real, y'all), we acknowledge that we didn't seak out any studies that would potentially challenge what we were already finding. (Although let it be known that from the bit of project creep we explored, our findings are pretty solid.)

## Resources
- [NOAA Atlantic Hurricane dataset](https://www.kaggle.com/datasets/utkarshx27/noaa-atlantic-hurricane-database)
- [stormglass.io Weather API](https://stormglass.io/marine-weather/)
- [NOAA Hurricane Satellite (HURSAT) Data](https://www.ncei.noaa.gov/products/hurricane-satellite-data)
- [Our World in Data | CO2 Emissions](https://ourworldindata.org/co2-emissions#%253A~%253Atext%253DBy%25201990%2520this%2520had%2520almost%252Cyet%2520to%2520reach%2520their%2520peak)

### Database
- SQLite

### Packages
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/graphing-libraries/)
- [Leaflet](https://leafletjs.com/)

## Presentation Slides
- https://docs.google.com/presentation/d/1m33rLC5GqkDEUTkYsn4l-ViKyNk9mXO5_uub1BL8pvU/edit#slide=id.gd5b15f0a3_5_26
