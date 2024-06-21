#!/usr/bin/python3
"""
This script lists all states with a name that matches
the argument from the database hbtn_0e_0_usa.
It takes 4 arguments: mysql username, mysql password,
database name, and state name searched.
The script is safe from MySQL injection.
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

    # Create the query with parameterized input to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
