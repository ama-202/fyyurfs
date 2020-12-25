
from flask_migrate import Migrate
from flask.app import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#i was here
class Show(db.Model):
  id = db.Column(db.Integer, primary_key=True,autoincrement=True)
  Venue_id=db.Column(db.Integer,db.ForeignKey('Venue.id'),primary_key=True)
  Artist_id=db.Column(db.Integer,db.ForeignKey('Artist.id'),primary_key=True)
  
  start_time=db.Column(db.DateTime())




  # venue_name=db.Column(db.Integer,db.ForeignKey('Venue.name'),primary_key=True)
  # artist_name=db.Column(db.Integer,db.ForeignKey('Artist.id'),primary_key=True)


  # db.Column('Venue_id',db.Integer,db.ForeignKey('Venue.id'),primary_key=True)
  # db.Column('Artist_id',db.Integer,db.ForeignKey('Artist.id'),primary_key=True)

  #migrate_engine.execute('
#here
  

  # def detail(self):
  #       return{
  #           'venue_id' :self.venue_id,
  #           'venue_name' :self.Venue.name,
  #           'artist_id' :self.artist_id,
  #           'artist_name' :self.Artist.name,
  #           'artist_image_link' :self.Artist.image_link,
  #           'start_time' :self.date
  #       }

#https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
  # venue = db.relationship('Venue' , back_populates='venues')
  # artist = db.relationship('Artist',back_populates='artists')

#here
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String , nullable=False)
    city = db.Column(db.String(120) ,nullable=False)
    state = db.Column(db.String(120),nullable=False)
    address = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    
    website = db.Column(db.String(120))

    genres = db.Column(db.String(120),nullable=False)
    
    seeking_talent=db.Column(db.Boolean, nullable=False, default=False)
    seeking_description=db.Column(db.String())

    shows = db.relationship('Show', backref="venue", lazy='dynamic')


class Artist(db.Model):
    __tablename__ = 'Artist' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    seeking_venue=db.Column(db.Boolean, nullable=False , default=False)
    seeking_description=db.Column(db.String())

    website = db.Column(db.String(120))
#https://stackoverflow.com/questions/11578070/sqlalchemy-instrumentedlist-object-has-no-attribute-filter
    shows = db.relationship('Show', backref="artist", lazy='dynamic')
    