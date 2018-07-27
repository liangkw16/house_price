#!/usr/bin/env python
# -*- coding: utf-8 -*-

#安装 MYSQL DB for python
import MySQLdb as mdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import math

class Point:
	pass

def max(a,b):
    if a>b:
        return a
    return b
def min(a,c):
    if a>c:
        return c
    return a

def lw(a, b, c):
#     b != n && (a = Math.max(a, b));
#     c != n && (a = Math.min(a, c));
    a = max(a,b)
    a = min(a,c)
    return a

def ew(a, b, c):
    
    while a > c:
        a -= c - b
    while a < b:
        a += c - b
    return a
        

def oi(a):
    return math.pi * a / 180

def Td(a, b, c, d): 
    return 6370996.81 * math.acos(math.sin(c) * math.sin(d) + math.cos(c) * math.cos(d) * math.cos(b - a))

def Wv(a, b):
    if not a or not b: 
        return 0;
    a.lng = ew(a.lng, -180, 180);
    a.lat = lw(a.lat, -74, 74);
    b.lng = ew(b.lng, -180, 180);
    b.lat = lw(b.lat, -74, 74);
    return Td(oi(a.lng), oi(b.lng), oi(a.lat), oi(b.lat))

def getDistance(a, b):
    c = Wv(a, b);
    return c


# 打开数据库连接
db= mdb.connect(
        host='166.111.80.177',
        port = 3306,
        user='lianjia',
        passwd='lianjia',
        db ='house',
        charset='utf8'
        )
# 使用cursor()方法获取操作游标 
cnt=0;
errcnt=0;
cursor = db.cursor()
sql = 'select * from ershou'
cursor.execute(sql)
rows = cursor.fetchall()

gate = Point()
gate.lng = 116.403963
gate.lat = 39.915119

for row in rows:
	id = row[0]
	p = Point()
	p.lng=row[7]
	p.lat=row[8]
	distance = getDistance(gate,p)
	try:
		cnt = cnt + 1
		# 执行sql语句
		cursor.execute('update ershou set distance='+str(distance)+' where id='+str(id))
		# 提交到数据库执行
		db.commit()
	except:
	# Rollback in case there is any error
		errcnt = errcnt + 1
		db.rollback()
# 关闭数据库连接
db.close()
print cnt,errcnt