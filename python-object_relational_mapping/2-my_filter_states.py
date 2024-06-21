#!/usr/bin/python3
"""
This script lists all states with a name that matches
the argument from the database hbtn_0e_0_usa.
It takes 4 arguments: mysql username, mysql password,
database name, and state name searched.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Capture the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Create the query with user input using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
