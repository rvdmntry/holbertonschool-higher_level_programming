#!/usr/bin/python3
"""
This script prints the first State object
from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username,
mysql password, and database name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
