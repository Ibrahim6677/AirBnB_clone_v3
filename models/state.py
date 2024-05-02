#!/usr/bin/python3
# """ State Module for HBNB project """
# import models
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship # type: ignore

# from models import storage_type
# from models.base_model import Base, BaseModel
# from models.city import City


# class State(BaseModel, Base):
#     """ State class / table model"""
#     __tablename__ = 'states'
#     if models.storage_t == 'db':
#         name = Column(String(128), nullable=False)
#         cities = relationship('City', backref='state',
#                               cascade='all, delete, delete-orphan')
#     else:
#         name = ""

#         @property
#         def cities(self):
#             '''returns the list of City instances with state_id
#                 equals the current State.id
#                 FileStorage relationship between State and City
#             '''
#             from models import storage
#             related_cities = []
#             cities = storage.all(City)
#             for city in cities.values():
#                 if city.state_id == self.id:
#                     related_cities.append(city)
#             return related_cities


""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list