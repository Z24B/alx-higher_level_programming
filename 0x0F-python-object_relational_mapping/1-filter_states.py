#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # MySQL connection parameters
    username = argv[1]
    password = argv[2]
    database = argv[3]

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

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
