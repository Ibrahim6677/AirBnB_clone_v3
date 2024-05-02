# #!/usr/bin/python3
# """This module defines a base class for all models in our hbnb clone"""
# import uuid
# import datetime
# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, String, DATETIME

# Base = declarative_base()

# class BaseModel:
#     """A base class for all hbnb models

#     Attributes:
#         id (sqlalchemy String): The BaseModel id.
#         created_at (sqlalchemy DateTime): The datetime at creation.
#         updated_at (sqlalchemy DateTime): The datetime of last update.
#     """
#     id = Column(String(60),
#                 nullable=False,
#                 primary_key=True,
#                 unique=True)
#     created_at = Column(DATETIME,
#                         nullable=False,
#                         default=datetime.datetime.utcnow)
#     updated_at = Column(DATETIME,
#                         nullable=False,
#                         default=datetime.datetime.utcnow)

#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model"""
#         if not kwargs:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.datetime.utcnow()
#             self.updated_at = datetime.datetime.utcnow()
#         else:
#             for k in kwargs:
#                 if k in ['created_at', 'updated_at']:
#                     setattr(self, k, datetime.datetime.fromisoformat(kwargs[k]))
#                 elif k != '__class__':
#                     setattr(self, k, kwargs[k])

#     def __str__(self):
#         """Returns a string representation of the instance"""
#         return '[{}] ({}) {}'.format(
#             self.__class__.__name__, self.id, self.__dict__)

#     def save(self):
#         """Updates updated_at with current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.datetime.utcnow()
#         storage.new(self)
#         storage.save()

#     def to_dict(self):
#         """Convert instance into dict format"""
#         dct = self.__dict__.copy()
#         dct['__class__'] = self.__class__.__name__
#         for k in dct:
#             if type(dct[k]) is datetime:
#                 dct[k] = dct[k].isoformat()
#         if '_sa_instance_state' in dct.keys():
#             del(dct['_sa_instance_state'])
#         return dct

#     def delete(self):
#         '''deletes the current instance from the storage'''
#         from models import storage
#         storage.delete(self)


#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if models.storage_t == 'db':
            if 'password' in new_dict:
                del new_dict['password']
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
