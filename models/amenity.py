# #!/usr/bin/python3
# """ State Module for HBNB project """
# from models.base_model import BaseModel, Base
# from models import storage_type
# from sqlalchemy import Column, String


# class Amenity(BaseModel, Base):
#     '''amenity class'''
#     __tablename__ = 'amenities'
#     if storage_type == 'db':
#         name = Column(String(128), nullable=False)
#     else:
#         name = ""


#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
