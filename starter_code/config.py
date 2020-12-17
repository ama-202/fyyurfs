import os 

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

app.config['SQLALCEMY_DATABASE_URI']='postgres://postgres:Mydata-00@localhost:5432/fyyurdb'


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
