#!/usr/bin/python3
"""Script to fetch all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query for City objects and sort them by id
    cities = session.query(City).order_by(City.id).all()

    # Display City objects along with their respective State names
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
