#!/usr/bin/python3
"""MySQL database connector"""
import sys
from MySQLdb import _mysql

if __name__="__main__":
    db=_mysql.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
