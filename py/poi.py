#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import MySQLdb as mdb
import sys
import math

reload(sys)
sys.setdefaultencoding('utf-8')

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


query = '购物'#地铁 1 公交 2 学校3 医院4 写字楼5 
queryType=6
radius='&radius=1000'
page_size='&page_size=20'
output = '&output=json'
ak = '&ak=dASz7ubuSpHidP1oQWKuAK3q'

# 打开数据库连接
db= mdb.connect(
        host='166.111.80.177',
        port = 3306,
        user='lianjia',
        passwd='lianjia',
        db ='house',
        charset='utf8'
        )
#db = mdb.connect('127.0.0.1', 'lianjia','lianjia', 'lianjia',charset='utf8');
# 使用cursor()方法获取操作游标 
cnt=0;
errcnt=0;
cursor = db.cursor()
sql = 'select * from ershou where id >=17908'
cursor.execute(sql)
rows = cursor.fetchall()

for i in range(len(rows)):
	row = rows[i]
	print 'houseid',row[0]
	houseid = row[0]
	houseP = Point()
	houseP.lng=row[7]
	houseP.lat=row[8]
	url = 'http://api.map.baidu.com/place/v2/search?query='
	location='&location='+str(houseP.lat)+','+str(houseP.lng)
	url = url + query +page_size+ location + radius + output + ak
	print url
	request = urllib2.urlopen(url)
	responce = request.read() 
	jsonObj = json.loads(responce)
	print jsonObj['message']
	results = jsonObj['results']
	cnt = 0
	for result in results:
		cnt = cnt + 1
		newP = Point()
		newP.lng = result['location']['lng']
		newP.lat = result['location']['lat']
		distance = getDistance(houseP,newP)

		insert = "insert into facility(house_id,name,address,longitude,latitude,type,distance) values(%d,'%s','%s',%f,%f,%d,%f)" % (houseid,result['name'],result['address'],result['location']['lng'],result['location']['lat'],queryType,distance)
		print insert
		
		try:
			cursor.execute(insert)
			#提交到数据库执行
		except Exception as e:
			# Rollback in case there is any error
			print 'insert error'
	print 'find records:',cnt
	sql1 = 'update ershou set subway_num=%d where id=%d' % (cnt,houseid)
	sql2 = 'update ershou set bus_num=%d where id=%d' % (cnt,houseid)
	sql3 = 'update ershou set school_num=%d where id=%d' % (cnt,houseid)
	sql4 = 'update ershou set hospital_num=%d where id=%d' % (cnt,houseid)
	sql5 = 'update ershou set work_num=%d where id=%d' % (cnt,houseid)
	sql6 = 'update ershou set shop_num=%d where id=%d' % (cnt,houseid)
	try:
		cursor.execute(sql6)
		#提交到数据库执行
		db.commit()
	except Exception as e:
		# Rollback in case there is any error
		print 'update error'
		db.rollback()
# 关闭数据库连接
db.close()
