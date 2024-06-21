#!/usr/bin/python3
"""
This module defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    City class that links to the MySQL table 'cities'.
    Attributes:
        id (int): Auto-generated, unique integer, primary key.
        name (str): String with a maximum of 128 characters, cannot be null.
        state_id (int): Integer, foreign key to states.id, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
