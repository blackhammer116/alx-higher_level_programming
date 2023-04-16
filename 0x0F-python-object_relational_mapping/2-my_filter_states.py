#!/usr/bin/python3
"""
    Script that takes a state name via command line argument
    and filters through the database

    using two modules MySQLdb and sys for database connection
    and for getting command line arguments
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Getting command line argument and executing the query
    """
    N = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(sys.argv[4],))
    query_fetch = cur.fetchall()
    for row in query_fetch:
        print(row)
    cur.close()
    db.close()
