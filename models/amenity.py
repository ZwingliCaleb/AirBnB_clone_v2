#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String

<<<<<<< HEAD
class Amenity(BaseModel, Base):
    """Class Amenity"""
=======

class Amenity(BaseModel, Base):
    """Represents amenity class"""
>>>>>>> 8cc433826609053dd785ce72883616c9f3b009af
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
