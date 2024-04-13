#!/usr/bin/python3
"""Script that changes the name of a State object"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with id=2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name of the State
    if state:
        state.name = "New Mexico"
        session.commit()
        session.close()
