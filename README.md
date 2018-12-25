# 北京房价可视化分析

This is a test.

## 数据
数据来自于链家网(https://bj.lianjia.com) 和百度地图，房源信息是链家网上2017年5月10日北京的25217条二手房信息，并根据二手房的坐标抓取了二手房附近的周边设施信息，包括地铁、公交、学校和医院等。

## 可视化设计

![image](https://github.com/liangkw16/house_price/blob/master/可视化设计.png)

### 1.房价分区对比

北京市有16个区2个县，不同区县的人文环境，地理环境和经济发展水平不同，房价自然会有差别，通过分区展示北京的房价，可以从宏观的角度来了解北京房价分布状况。

![image](https://github.com/liangkw16/house_price/blob/master/总体分布.png)

### 2.房价散点图

每一套二手房有对应的坐标和单价信息，可以将每一套二手房当做一个点，单价高低进行颜色编码，在地理坐标空间中绘制散点图，用最简单的方式来展示北京房价分布。

![image](https://github.com/liangkw16/house_price/blob/master/散点图.png)

### 3.房价热力图

使用一定大小的经纬度步长来将北京划分为众多小区域，用不同颜色来编码房价水平，房价越高颜色越深，这样就能够绘制出北京房价的热力图，可以更精细地展现北京房价的分布情况。

![image](https://github.com/liangkw16/house_price/blob/master/热力图.png)

### 4.房价等价图

类似于等高线和等温线，这里将绘制出北京房价的等价图，从而勾勒出北京房价内在的分布规律，以便更好的了解北京房价的具体情况。

![image](https://github.com/liangkw16/house_price/blob/master/等价线.png)

### 5.周边设施可视化

以上四种方式展示了北京房价的分布情况，从中可以得到很多关于北京房价分布的规律，这里通过对房子周边设施的可视化分析，来解释房价分布规律出现的原因。

![image](https://github.com/liangkw16/house_price/blob/master/房屋周边.png)

## 技术说明
1. Web——ThinkPHP
2. 数据库——Mysql
3. 地图——百度地图插件
4. 可视化——Echarts.js, Maobox GL
5. 爬虫——scrapy
