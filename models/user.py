#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore

from models.base_model import storage_type, BaseModel, Base

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if models.storage_t == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""


def __init__(self, *args, **kwargs):
        """initializes user"""
        if 'password' in kwargs:
            kwargs['password'] = hashlib.md5(kwargs['password']
                                             .encode()).hexdigest()
        super().__init__(*args, **kwargs)
