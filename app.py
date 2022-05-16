# 9.4.3 Set Up Flask and Create a Route
# 1.) Install Flask.
# 2.) Create a new Python file.
# 3.) Import the Flask dependency.
# 4.) Create a new Flask app instance.
# 5.) Create Flask routes.
# 6.) Run a Flask app

# Set Up the Flask Weather App
# Create a New Python File and Import the Flask Dependency
#from flask import Flask
#import datetime as dt
#from lib2to3.pytree import _Results
#import numpy as np
#import pandas as pd
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func
# from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set Up the Database
# Set Up the database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")
# get access and query ability to the SQLite database file
Base = automap_base()
# reflect the database:
Base.prepare(engine, reflect=True)
# View Classes Found by Automap
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to database
session = Session(engine)
results = session.query

# Define our app for our Flask application
# Create a New Flask App Instance
app = Flask(__name__)
import app
print("example __name__ = %s", __name__)
if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

# 9.5.2 Create Flask Welcome Route
# Create Flask Routes
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# 9.5.3 Create Flask Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# 9.5.4 Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# 9.5.5 Monthly Temperature Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# 9.5.6 Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Run a Flask App
# 1.) In Anaconda Navigator or in Git Bash.
## a.) If runing in Git Bash make sure to open the Python Data in the Conda Environment, this has PIP
## a.1.) 
# set FLASK_APP=app.py
# 
# flask run