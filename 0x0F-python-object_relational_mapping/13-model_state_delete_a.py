#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a"""
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

    # Query for State objects with a name containing the letter "a"
    states_with_a = session.query(State).filter(State.name.like("%a%")).all()

    # Delete the State objects
    for state in states_with_a:
        session.delete(state)
        session.commit()
        session.close()
