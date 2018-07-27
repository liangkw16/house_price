/**
 * Created by Di Qi on 14/06/2017.
 */

// 用Mapbox GL绘制地图
var map;
var initMap = function () {
    mapboxgl.accessToken = 'pk.eyJ1Ijoid2FuZ3h1MTk5MyIsImEiOiJjaXFudXgyMzQwMWdoZ2lqZm15NWdjdTJ2In0.tsx6buZEC4a9oWbFH2CcSQ';
    map = new mapboxgl.Map({
        'container': '7dmap',
        'style': 'mapbox://styles/mapbox/light-v9',
        'hash': true,
        'center': [116.4344, 39.9335],
        'zoom': 9.33,
        'maxZoom': 13
    });
    map.addControl(new mapboxgl.ScaleControl({
        maxWidth: 100,
        unit: 'metric'
    }));
    // map.addControl(new mapboxgl.NavigationControl(), 'bottom-left');
};

// 载入房价数据后保存
var total_houses = [];
var loadData = function () {
    $.ajax({
        url: "/house_price/Home/Index/get_all",
        data: {
            price: 0,
            area: 0,
            distance: 0
        },
        dataType: 'json',
        success: function (data) {
            $.each(data, function(i, d) {
                total_houses.push([d['longitude'], d['latitude'], d['unit_price'] / 1e4]);
            });
            console.log("Load Data: " + total_houses.length);
            // 载入完成后，回调绘图函数
            drawGraph();
        }
    });
};

// 将经纬度坐标映射为屏幕坐标
var pointProject = function (lng, lat) {
    var p = map.project(new mapboxgl.LngLat(lng, lat));
    return [p.x, p.y];
};

// 获得屏幕显示的经纬度的边界
var getBoundList = function () {
    var bounds = map.getBounds();
    return [bounds.getNorth(), bounds.getEast(), bounds.getSouth(), bounds.getWest()];
};

var drawGraph = function () {
    // 初始化画布(SVG)
    var initSVG = function () {
        var container = map.getCanvasContainer();
        var svg = d3.select(container).append('svg');
        return svg;
    };
    var svg = initSVG();
    var width = $('svg').width();
    var height = $('svg').height();

    // 获取房价范围
    var minp = Math.floor(d3.min(total_houses, function(d) { return d[2]; }));
    var maxp = Math.ceil(d3.max(total_houses, function(d) { return d[2]; })) + 1;
    console.log(minp, maxp);

    // 将房价范围与colormap关联
    var i0 = d3.interpolateHsvLong(d3.hsv(120, 1, 0.65), d3.hsv(60, 1, 0.90)),
        i1 = d3.interpolateHsvLong(d3.hsv(60, 1, 0.90), d3.hsv(0, 0, 0.95)),
        interpolateTerrain = function(t) { return t < 0.5 ? i0(t * 2) : i1((t - 0.5) * 2); },
        color = d3.scaleSequential(interpolateTerrain).domain([minp, maxp]);

    // 清空画布
    var clear = function () {
        svg.selectAll('*').remove();
    };
    // 根据屏幕范围内的数据点，绘制等高线
    var render = function () {
        var bound_list = getBoundList();
        var visible_houses = total_houses.filter(function (d) {
            return (bound_list[3] <= d[0] && d[0] <= bound_list[1]
                    && bound_list[2] <= d[1] && d[1] <= bound_list[0]);
        });     // 保留屏幕范围内的数据
        visible_houses = visible_houses.map(function (d) {
            var lng_lat = pointProject(d[0], d[1]);
            return [lng_lat[0], lng_lat[1], d[2]];
        });     // 将经纬度坐标转换为屏幕坐标

        clear();
        // 显示散点图
        // svg.selectAll('circle')
        //     .data(visible_houses)
        //     .enter()
        //     .append('circle')
        //     .attr('cx', function (d) { return d[0]; })
        //     .attr('cy', function (d) { return d[1]; })
        //     .attr('r', 2)
        //     .attr('fill', function(d) { return color(d[2]); });

        var thresholds = 15;    // 等高线的条数
        var paths = d3.contourDensity().size([width, height]).cellSize(2).thresholds(thresholds)(visible_houses);
        var max_path_value = d3.max(paths, function(d) { return d.value; });
        var max_point_value = d3.max(visible_houses, function(d) { return d[2]; });
        var coef = max_point_value / max_path_value;

        svg.selectAll("path")
            .data(paths)
            .enter()
            .append("path")
            .attr("d", d3.geoPath())
            .attr("stroke", function(d) { return color(d.value * coef); })
            .attr("stroke-width", 2)
            .attr("fill", "transparent");
    };
    render();

    // 在屏幕变化时重新绘图
    map.on('viewreset', function () { render(); });
    map.on('movestart', function () { clear(); });
    map.on('moveend', function () { render(); });
    map.on('load', function () { render(); });
};

$(document).ready(function () {
    initMap();
    loadData();
});
