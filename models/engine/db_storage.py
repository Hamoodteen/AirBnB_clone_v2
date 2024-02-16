#!/usr/bin/python3
""" New engine DBStorage """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


classes = {
    # 'BaseModel': BaseModel,
    'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """ DBStorage Class """
    __engine = None

    def __init__(self):
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        
    def reload(self, removed=False):
        """cccccccccccccccccccccccccccccccccccc"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        if removed:
            Session.remove()
        self.__session = Session()

    def close(self):
        """ccccccccccccccccccccccc"""
        self.reload(removed=True)
