#!/usr/bin/python3
"""Script that lists all cities"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    # Fetch all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
