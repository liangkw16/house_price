#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
file = open('ershouold.json','r')  
newfile = open('ershou.sql','w')
count =0
errcount = 0
lines = file.readlines()

for line in lines:
	count = count + 1
	flag = False;
	record = {}
	try:
		data = json.loads(line)
		record['housearea']=data[u'housearea'][:-1]
		record['longitude'] = data[u'latitude'].split(',')[0]
		record['latitude']= data[u'latitude'].split(',')[1]
		record['unit_price']=data[u'unit_price']
		record['community']=data[u'community']
		record['style']=data[u'style']
		record['area'] = data[u'area']
		record['url'] = data[u'url']
		record['floor'] = data[u'floor']

	except Exception as e:
		errcount = errcount + 1
		flag = True
	else:
		pass
	finally:
		if flag:
			print count
			print 'test'
		else:
			str='insert into ershou(';
			for key in record.keys():
				str = str + key + ','
			str = str[:-1]
			str = str +') values('
			for key in record.keys():
				if key=='housearea' or key=='longitude' or  key=='latitude' or key=='unit_price':
					str = str + record[key]+','
				else:
					str = str + "'" + record[key] +"',"
			str = str[:-1]
			str = str + ');\n'
			newfile.write(str)
print count
print errcount