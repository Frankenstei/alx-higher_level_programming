#!/usr/bin/python3
"""MySQL database connector"""
import sys
from MySQLdb import _mysql

if __name__="__main__":
    db=_mysql.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], match=sys.arg[4])
    cur = db.cursor
    cur.execute("SELECT * FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in cur.fetchall() if c[4] == match]))]
