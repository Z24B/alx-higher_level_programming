#!/usr/bin/python3
"""Script that displays all values in the states"""
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
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))

    # Fetch all rows
    rows = cur.fetchall()

    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
