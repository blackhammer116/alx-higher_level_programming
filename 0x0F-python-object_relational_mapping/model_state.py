#!/usr/bin/python3
"""
    Script that creates a class state and intergrated with the table

    Using SQLAlchemy module
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        State class which will be later integrated with states table

        Attributes:
            __tablename__ (str): name of the table in use
            id (int): id of the state
            name (str): name of the state
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
