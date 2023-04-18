#!/usr/bin/python3
"""
    Script that lists all staets ordered by state.id

    Using MySQLdb, sys and SQLAlchemy
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    """
        Here we create an engine, create an instance of Session and
        list all states based on our objects not query
    """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    S = session.query(State).filter(State.name == argv[4]).first()
    if S:
        print("{0}".format(S.id))
    else:
        print("Not found")
    session.close()
