#!/usr/bin/python3
""" imports mysql database """
""" imports system in order to take in command line argument """
import sys
import MySQLdb


if __name__ == "__main__":
    """ listes all of the states in ascending order """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_fetch = cur.fetchall()
    for row in query_fetch:
        print(row)
    cur.close()
    db.close()
