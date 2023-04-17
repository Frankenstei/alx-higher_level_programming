#!/usr/bin/python3
"""MySQL database connector"""
import sys
import MySQLdb

if __name__="__main__":
    db=MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
