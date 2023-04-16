#!/usr/bin/python3
import sys
""" imports system inorder to take in command line argument """
import MySQLdb
""" imports mysql database """


User = sys.argv[1]
password = sys.argv[2]
database = sys.argv[2]
db = MySQLdb.connect(host = "localhost", port = 3306, user = User, passwd = password, db = database, charset = "utf8")
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
query_fetch = cur.fetchall()

for row in query_fetch:
    print (row)
cur.close()
db.close()
