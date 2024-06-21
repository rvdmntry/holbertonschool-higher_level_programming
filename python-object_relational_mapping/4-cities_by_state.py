#!/usr/bin/python3
"""
This script lists all cities from the
database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password,
and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Capture the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

    # Execute the query to select all cities with their state names
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    db.close()
