#!/usr/bin/python3
"""Script lists all cities of a state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
            )

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query safely
    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch all rows
    row = cur.fetchone()

    # Display results
    if row[0]:
        print(row[0])
    else:
        print("")

    # Close cursor and database connection
    cur.close()
    db.close()
