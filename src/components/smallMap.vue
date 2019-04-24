<template>
	<div id="samllMap" style="width:25%;height: 100%;"></div>
</template>

<script>
	import { mapjs } from '../../static/js/china.js'
	import $ from 'jquery'
	import * as echarts from 'echarts'
	export default {
		name: "smallmap",
		mounted() {
			var myChart = echarts.init(document.getElementById('samllMap'));
			var option = null

			var geoCoordMap = {
				'甘肃': [103.73, 36.03],
				'青海': [101.74, 36.56],
				'四川': [104.06, 30.67],
				'河北': [114.48, 38.03],
				'云南': [102.73, 25.04],
				'贵州': [106.71, 26.57],
				'湖北': [114.31, 30.52],
				'河南': [113.65, 34.76],
				'山东': [117, 36.65],
				'江苏': [118.78, 32.04],
				'安徽': [117.27, 31.86],
				'浙江': [120.19, 30.26],
				'江西': [115.89, 28.68],
				'福建': [119.3, 26.08],
				'广东': [113.23, 23.16],
				'湖南': [113, 28.21],
				'海南': [110.35, 20.02],
				'辽宁': [123.38, 41.8],
				'吉林': [125.35, 43.88],
				'黑龙江': [126.63, 45.75],
				'山西': [112.53, 37.87],
				'陕西': [108.95, 34.27],
				'台湾': [121.30, 25.03],
				'北京': [116.46, 39.92],
				'上海': [121.48, 31.22],
				'重庆': [106.54, 29.59],
				'天津': [117.2, 39.13],
				'内蒙古': [111.65, 40.82],
				'广西': [108.33, 22.84],
				'西藏': [91.11, 29.97],
				'宁夏': [106.27, 38.47],
				'新疆': [87.68, 43.77],
				'香港': [114.17, 22.28],
				'澳门': [113.54, 22.19]
			};

			//var BJData = [[{'name': '北京', 'value': 1}, {'name': '重庆'}], [{'name': '天津', 'value': 1}, {'name': '重庆'}], [{'name': '河北', 'value': 23}, {'name': '重庆'}], [{'name': '山西', 'value': 18}, {'name': '重庆'}], [{'name': '内蒙古', 'value': 11}, {'name': '重庆'}], [{'name': '辽宁', 'value': 10}, {'name': '重庆'}], [{'name': '吉林', 'value': 9}, {'name': '重庆'}], [{'name': '黑龙江', 'value': 13}, {'name': '重庆'}], [{'name': '上海', 'value': 1}, {'name': '重庆'}], [{'name': '江苏', 'value': 25}, {'name': '重庆'}], [{'name': '浙江', 'value': 22}, {'name': '重庆'}], [{'name': '安徽', 'value': 31}, {'name': '重庆'}], [{'name': '福建', 'value': 21}, {'name': '重庆'}], [{'name': '江西', 'value': 33}, {'name': '重庆'}], [{'name': '山东', 'value': 21}, {'name': '重庆'}], [{'name': '河南', 'value': 50}, {'name': '重庆'}], [{'name': '湖北', 'value': 77}, {'name': '重庆'}], [{'name': '湖南', 'value': 54}, {'name': '重庆'}], [{'name': '广东', 'value': 19}, {'name': '重庆'}], [{'name': '广西', 'value': 14}, {'name': '重庆'}], [{'name': '海南', 'value': 7}, {'name': '重庆'}], [{'name': '四川', 'value': 1249}, {'name': '重庆'}], [{'name': '贵州', 'value': 137}, {'name': '重庆'}], [{'name': '云南', 'value': 47}, {'name': '重庆'}], [{'name': '西藏', 'value': 6}, {'name': '重庆'}], [{'name': '重庆', 'value': 0}, {'name': '重庆'}], [{'name': '陕西', 'value': 29}, {'name': '重庆'}], [{'name': '甘肃', 'value': 25}, {'name': '重庆'}], [{'name': '青海', 'value': 7}, {'name': '重庆'}], [{'name': '宁夏', 'value': 5}, {'name': '重庆'}], [{'name': '新疆', 'value': 21}, {'name': '重庆'}]]

			var BJData = [
				[{
					'name': '北京',
					'value': 7
				}, {
					'name': '重庆'
				}],
				[{
					'name': '天津',
					'value': 7
				}, {
					'name': '重庆'
				}],
				[{
					'name': '河北',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '山西',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '内蒙古',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '辽宁',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '吉林',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '黑龙江',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '上海',
					'value': 7
				}, {
					'name': '重庆'
				}],
				[{
					'name': '江苏',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '浙江',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '安徽',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '福建',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '江西',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '山东',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '河南',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '湖北',
					'value': 11
				}, {
					'name': '重庆'
				}],
				[{
					'name': '湖南',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '广东',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '广西',
					'value': 9
				}, {
					'name': '重庆'
				}],
				[{
					'name': '海南',
					'value': 8
				}, {
					'name': '重庆'
				}],
				[{
					'name': '四川',
					'value': 14
				}, {
					'name': '重庆'
				}],
				[{
					'name': '贵州',
					'value': 11
				}, {
					'name': '重庆'
				}],
				[{
					'name': '云南',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '西藏',
					'value': 8
				}, {
					'name': '重庆'
				}],
				[{
					'name': '重庆',
					'value': 0
				}, {
					'name': '重庆'
				}],
				[{
					'name': '陕西',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '甘肃',
					'value': 10
				}, {
					'name': '重庆'
				}],
				[{
					'name': '青海',
					'value': 8
				}, {
					'name': '重庆'
				}],
				[{
					'name': '宁夏',
					'value': 8
				}, {
					'name': '重庆'
				}],
				[{
					'name': '新疆',
					'value': 9
				}, {
					'name': '重庆'
				}]
			]

			var convertData = function(data) {
				var res = [];
				for(var i = 0; i < data.length; i++) {
					var dataItem = data[i];
					var fromCoord = geoCoordMap[dataItem[0].name];
					var toCoord = geoCoordMap[dataItem[1].name];
					if(fromCoord && toCoord) {
						res.push({
							fromName: dataItem[0].name,
							toName: dataItem[1].name,
							coords: [fromCoord, toCoord]
						});
					}
				}
				return res;
			};

			/*var covertColor = function(data) {
				var value = data[1].value;
				var result = 'aqua';
				if(value >= 13) {
					result = '#ff3333';
				} else if(value >= 12) {
					result = 'orange';
				} else if(value >= 10) {
					result = 'yellow';
				} else {
					result = 'lime';
				}
				return result;
			};*/

			var series = [];
			[
				['北京', BJData]
			].forEach(function(item, i) {
				series.push({
					name: item[2],
					type: 'lines',
					zlevel: 2,
					effect: {
						show: true,
						period: 6,
						trailLength: 0.1,
						//            symbol: planePath,
						symbol: 'arrow',
						symbolSize: 5
					},
					lineStyle: {
						normal: {
							color: '#004882',
							width: 1,
							opacity: 0.4,
							curveness: 0.2
						}
					},
					data: convertData(item[1])
				}, {
					//       name: item[1],
					type: 'effectScatter',
					coordinateSystem: 'geo',
					zlevel: 2,
					rippleEffect: {
						brushType: 'stroke'
					},
					label: {
						normal: {
							show: true,
							position: 'right',
							formatter: '{b}'
						}
					},
					symbolSize: function(val) {
						//console.log(val)
						if (val[2]>=11) return val[2];
						else if (val[2]==10) return val[2]/2;
						else if (val[2]==9)  return val[2]/3;
						else return 1;
					},
					itemStyle: {
						normal: {
							color: '#fff'
						}
					},
					data: item[1].map(function(dataItem) {
						return {
							name: dataItem[0].name,
							value: geoCoordMap[dataItem[0].name].concat([dataItem[0].value])
						};
					})
				});
			});

			option = {
				//backgroundColor: '#363636',
				title: {
					text: '外来人口分布',
					left: 'center',
					textStyle: {
						color: '#fff'
					}
				},
				tooltip: {
					trigger: 'item'
				},
				geo: {
					map: 'china',
					label: {
						emphasis: {
							show: false
						}
					},
					roam: true,
					itemStyle: {
						normal: {
							areaColor: 'rgb(128, 185, 218)',
							borderColor: '#20a6C7'
						},
						emphasis: {
							areaColor: '#2a333d'
						}
					}
				},
				series: series
			};

			if(option && typeof option === "object") {
				myChart.setOption(option, true);
			}

		}
	}
</script>

<style>

</style>