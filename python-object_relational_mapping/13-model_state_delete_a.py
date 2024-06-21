#!/usr/bin/python3
"""
This script deletes all State objects with
a name containing the letter 'a'
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

    # Query all State objects with a name containing the letter 'a'
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    # Delete the state objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
