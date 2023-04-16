#!/usr/bin/python3
"""
    Script that lists all cities by ascending order

    Using modules MySQLdb and sys for database access and getting user input
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
        Getting user input, making database connections, and listing cities
    """
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name, cities.id FROM cities JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = (%s) ORDER BY cities.id ASC", (sys.argv[4],))
    query_fetch = cur.fetchall()
    print(", ".join([row[0] for row in query_fetch]))
    cur.close()
    db.close()
