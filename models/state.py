#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            """ Method that gets cities"""
            cityls = []
            for cityid in models.storage.all(City).values():
                if getattr(cityid, "state_id") == self.id:
                    cityls.append(cityid)
            return(cityls)
