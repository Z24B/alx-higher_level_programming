#!/usr/bin/python3
"""Script that adds the State object "Louisiana" """
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

    # Create State object for Louisiana
    new_state = State(name="Louisiana")

    # Add State object to session
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)
    session.close()
