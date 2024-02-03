import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Hurricane_Weather.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine, reflect=True)

# Save reference to the table
Dorain_Abaco = Base.classes.Dorain_Abaco
Dorian_MB = Base.classes.Dorian_MB
Dorian_Will = Base.classes.Dorian_Will

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/data/Abaco", methods=['GET'])
def get_data_abaco():
    # create session (link from python to db)
    session = Session(engine)

    # query the desired columns
    results = session.query(Dorain_Abaco.time, Dorain_Abaco.airTemperature_noaa).all()

    # close the session
    session.close()

    # Convert the results to a list of dictionaries with formatted time
    data = [{'time': format_datetime(result.time), 'air_temperature_noaa': result.airTemperature_noaa} for result in results]

    # Create a JSON response
    response = jsonify(data)

    # Allow cross-origin resource sharing
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/api/data/Myrtle_Beach", methods=['GET'])
def get_data_mb():
    # create session (link from python to db)
    session = Session(engine)

    # query the desired columns
    results = session.query(Dorian_MB.time, Dorian_MB.airTemperature_noaa).all()

    # close the session
    session.close()

    # Convert the results to a list of dictionaries with formatted time
    data = [{'time': format_datetime(result.time), 'air_temperature_noaa': result.airTemperature_noaa} for result in results]

    # Create a JSON response
    response = jsonify(data)

    # Allow cross-origin resource sharing
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/api/data/Wilmington", methods=['GET'])
def get_data_will():
    # create session (link from python to db)
    session = Session(engine)

    # query the desired columns
    results = session.query(Dorian_Will.time, Dorian_Will.airTemperature_noaa).all()

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
