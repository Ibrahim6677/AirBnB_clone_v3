# #!/usr/bin/python3
# """ City Module for HBNB project """
# from models.base_model import BaseModel, Base
# from models import storage_type
# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship


# class City(BaseModel, Base):
#     """ The city class, contains state ID and name """
#     __tablename__ = 'cities'
#     if storage_type == 'db':
#         name = Column(String(128), nullable=False)
#         state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
#         places = relationship('Place', backref='cities',
#                               cascade='all, delete, delete-orphan')
#     else:
#         name = ''
#         state_id = ''


#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
