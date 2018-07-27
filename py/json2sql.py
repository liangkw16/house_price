import json  
  
  
file = open('data.json','r')
datas = json.load(file)
#print json.dumps(data, ensure_ascii=False)  
  
str = ''  
for item in datas:  
    #print json.dumps(item)  
    str =str + "insert into houses(created_at, longitude, floor, url, average_price, area, distance, \
   updated_at, build_time, hospital_num, work_num, street, subway_num, community, school_num,\
    latitude, room_shape, bus_num, id, shop_num) values ('%s',%f,'%s','%s',%d,%d,%f,'%s','%s',\
    %d,%d,'%s',%d,'%s',%d,'%f','%s',%d,%d,%d)" % (item['created_at'],float(item['longitude']),item['floor'],item['url'],
    	int(item['average_price']),int(item['area']),float(item['distance']),item['updated_at'],item['build_time'],int(item['hospital_num']),int(item['work_num']),item['street'],
    	int(item['subway_num']),item['community'],int(item['school_num']),float(item['latitude']),item['room_shape'],int(item['bus_num']),int(item['id']),int(item['shop_num']))
    str=str+';\n'
  
import codecs  
file_object = codecs.open('house.sql', 'w' ,"utf-8")  
file_object.write(str)  
file_object.close()  
print "success"  