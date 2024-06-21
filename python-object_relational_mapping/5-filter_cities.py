#!/usr/bin/python3
"""
This script lists all cities of a given state from
the database hbtn_0e_4_usa.
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
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results as a comma-separated string
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and connection
    cursor.close()
    db.close()
