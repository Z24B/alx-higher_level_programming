#!/usr/bin/python3
"""Script that lists all cities of a given state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    state_name = argv[4]

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

    # Execute SQL query safely
    query = """
    SELECT GROUP_CONCAT(DISTINCT cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch the result
    result = cur.fetchone()[0]
    if result:
        print(result)
    else:
        print("")

    cur.close()
    db.close()
