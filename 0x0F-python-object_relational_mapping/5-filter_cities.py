#!/usr/bin/python3
"""Script that lists all cities of a given state"""
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
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))

    # Fetch unique city names
    cities = set(row[0] for row in cur.fetchall())
    print(", ".join(cities))
    cur.close()
    db.close()
