from sys import stdin
from sys import stdout
import MySQLdb
from MySQLdb import cursors
from datetime import date
from datetime import timedelta

#db = MySQLdb.connect(host='172.16.130.56', user='readuser', passwd='password', db='ProductDB', cursorclass=cursors.SSCursor) 
#sql_string = 'select product_id, category_id, product_name, brand  from Products_Core'


db = MySQLdb.connect(host='192.168.225.142', user='reader', passwd='n0p4ssw0rd', db='search_info', cursorclass=cursors.SSCursor) 
#sql_string = 'select * from all_pid_key'
#sql_string = 'show tables'


def dump_table(cur, sql_string, output):
    cur.execute(sql_string)
    f = open(output,'w')
    for row in cur:
        line = reduce(lambda x,y:str(x)+'\t'+str(y), row)
        f.writelines(line + '\n')
    f.close()

day = date(2013, 10, 11)
end_day = date(2013, 12, 26)
cur = db.cursor()
while day < end_day:
    sql_string = 'select * from key_cat_%s' % day.strftime('%Y%m%d')
    output = 'search_info_key_cat/key_cat_%s' % day.strftime('%Y%m%d')
    print(sql_string)
    day = day + timedelta(1)
    try:
        dump_table(cur, sql_string, output)
    except:
        print('execute error: [%s]' % sql_string)
        continue

#cur.execute(sql_string)
#for row in cur:
#    line = reduce(lambda x,y:str(x)+'\t'+str(y), row)
#    print(line)
