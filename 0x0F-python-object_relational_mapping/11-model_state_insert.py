#!/usr/bin/python3
"""
    Script that adds a new state object
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    """
        creating a new object and adding it to the DB
    """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    N = session.query(State).filter(State.name == 'Louisiana').first()
    print("{0}".format(N.id))
    session.close()
