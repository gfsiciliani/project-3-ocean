import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///weather.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine, reflect=True)

# Save reference to the table
Weather = Base.classes.weather

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/data", methods=['GET'])
def get_data():
    # create session (link from python to db)
    session = Session(engine)

    # query the desired columns
    results = session.query(Weather.time, Weather.airTemperature_noaa).all()

    # close the session
    session.close()

    # Convert the results to a list of dictionaries with formatted time
    data = [{'time': format_datetime(result.time), 'air_temperature_noaa': result.airTemperature_noaa} for result in results]

    # Create a JSON response
    response = jsonify(data)

    # Allow cross-origin resource sharing
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

def format_datetime(time_str):
    # Convert the string to a datetime object
    datetime_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S+00:00')

    # Format the datetime object as a string
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run()
