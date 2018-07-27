#!/usr/bin/env python
# -*- coding: utf-8 -*-

#安装 MYSQL DB for python
import MySQLdb as mdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open('ershou.sql','r')
# 打开数据库连接
db = mdb.connect('127.0.0.1', 'root','123456', 'lianjia',charset='utf8');
# 使用cursor()方法获取操作游标 
cnt=0;
errcnt=0;
cursor = db.cursor()

for line in file.readlines():
    line=line.strip('\n')
    #print line
    try:
      cnt = cnt + 1
      # 执行sql语句
      cursor.execute(line)
      # 提交到数据库执行
      db.commit()
    except:
    # Rollback in case there is any error
      errcnt = errcnt + 1
      db.rollback()

# 关闭数据库连接
db.close()
print cnt,errcnt