# coding: utf-8
import sys
from sys import stdin
from sys import stdout
from sys import stderr

import time
import MySQLdb
from MySQLdb import cursors


db = MySQLdb.connect(host='172.16.130.56', user='readuser', passwd='password', db='ProductDB', cursorclass=cursors.SSCursor) 
cur = db.cursor()


def get_result(cur):
    for row in cur:
        print(row[0])

n = 0
for line in stdin:
    pid = line.rstrip()
    sql_string = 'select product_name, brand from Products_Core where product_id = ' + pid 
    cur.execute(sql_string)
    for row in cur:
        print(pid + '\t' + row[0])
    if n % 100 == 0:
        stderr.writelines(str(n) + '\n')
    n+=1 
    time.sleep(0.02)

