#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places_id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenity')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Get list of all linked Reviews"""
            from models import storage
            review_lst = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_lst.append(review)
            return review_lst

        @property
        def amenities(self):
            """get/set linked amenities"""
            from models import storage
            amenity_lst = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenit_ids:
                    amenity_lst.append(amenity)
                return amenity_lst

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
