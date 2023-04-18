#!/usr/bin/python3
"""
    Script that lists all staets ordered by state.id

    Using MySQLdb, sys and SQLAlchemy
"""
import sys
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
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
