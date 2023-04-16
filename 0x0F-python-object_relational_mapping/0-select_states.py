#!/usr/bin/python3
import sys
""" imports system inorder to take in command line argument """
import MySQLdb
""" imports mysql database """


if __name__ == "__main__":
    """ This function listes all of the states in ascending order """

    U = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[2]
    db = MySQLdb.connect(host="localhost", port=3306, user=U, passwd=p, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_fetch = cur.fetchall()
    for row in query_fetch:
        print(row)
    cur.close()
    db.close()
