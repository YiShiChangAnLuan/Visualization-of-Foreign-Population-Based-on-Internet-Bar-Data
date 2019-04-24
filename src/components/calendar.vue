<template>
	<div id="calendar" style="height: 50%;"></div>
</template>

<script>
	import * as echarts from 'echarts'
	import axios from 'axios'
	import $ from 'jquery'
	export default {
		name: "calendar",
		data() {
			return {
				data: [],
				unit: 2000
			}
		},
		mounted() {
			let me = this;
			// 基于准备好的dom，初始化echarts实例
			var myChart = echarts.init(document.getElementById('calendar'));

			me.data = [
				['2016-10-01', 22843],
				['2016-10-02', 20702],
				['2016-10-03', 20628],
				['2016-10-04', 19543],
				['2016-10-05', 19175],
				['2016-10-06', 19395],
				['2016-10-07', 18421],
				['2016-10-08', 16118],
				['2016-10-09', 16523],
				['2016-10-10', 14933],
				['2016-10-11', 15296],
				['2016-10-12', 14982],
				['2016-10-13', 15589],
				['2016-10-14', 18317],
				['2016-10-15', 21463],
				['2016-10-16', 20241],
				['2016-10-17', 15459],
				['2016-10-18', 15001],
				['2016-10-19', 15160],
				['2016-10-20', 15414],
				['2016-10-21', 18320],
				['2016-10-22', 21662],
				['2016-10-23', 21582],
				['2016-10-24', 15414],
				['2016-10-25', 15618],
				['2016-10-26', 14914],
				['2016-10-27', 15767],
				['2016-10-28', 18495],
				['2016-10-29', 21397],
				['2016-10-30', 19863],
				['2016-10-31', 15338],
				['2016-11-01', 30436],
				['2016-11-02', 30237],
				['2016-11-03', 30255],
				['2016-11-04', 36347],
				['2016-11-05', 42623],
				['2016-11-06', 38485],
				['2016-11-07', 29319],
				['2016-11-08', 28639],
				['2016-11-09', 30249],
				['2016-11-10', 30276],
				['2016-11-11', 35895],
				['2016-11-12', 37919],
				['2016-11-13', 38458],
				['2016-11-14', 29323],
				['2016-11-15', 29003],
				['2016-11-16', 29433],
				['2016-11-17', 30800],
				['2016-11-18', 36300],
				['2016-11-19', 42210],
				['2016-11-20', 40233],
				['2016-11-21', 30737],
				['2016-11-22', 30420],
				['2016-11-23', 30634],
				['2016-11-24', 30333],
				['2016-11-25', 35357],
				['2016-11-26', 40549],
				['2016-11-27', 38004],
				['2016-11-28', 28310],
				['2016-11-29', 32663],
				['2016-11-30', 32801],
				['2016-12-01', 15722],
				['2016-12-02', 18488],
				['2016-12-03', 21998],
				['2016-12-04', 19532],
				['2016-12-05', 14766],
				['2016-12-06', 14816],
				['2016-12-07', 14778],
				['2016-12-08', 15259],
				['2016-12-09', 17599],
				['2016-12-10', 20548],
				['2016-12-11', 19457],
				['2016-12-12', 15126],
				['2016-12-13', 15747],
				['2016-12-14', 15186],
				['2016-12-15', 15911],
				['2016-12-16', 18306],
				['2016-12-17', 20905],
				['2016-12-18', 19692],
				['2016-12-19', 15360],
				['2016-12-20', 14602],
				['2016-12-21', 9599],
				['2016-12-22', 14338],
				['2016-12-23', 16808],
				['2016-12-24', 20332],
				['2016-12-25', 19577],
				['2016-12-26', 15728]
			];

			var option = {

				title: {
					top: 5,
					text: '',
					left: 'center',
					textStyle: {
						color: '#000'
					}
				},
				tooltip: {
					trigger: 'item',
					formatter: function(params) {
						return params.data[1] + '人次';
					}
				},
				legend: {
					top: '10',
					left: 'center',
					data: ['TimeLog', 'Top 12'],
					textStyle: {
						color: '#fff'
					}
				},
				calendar: [{
					top: 45,
					left: 'center',
					range: ['2016-10-01', '2016-12-26'],
					splitLine: {
						show: true,
						lineStyle: {
							color: '#fff',
							width: 4,
							type: 'solid'
						}
					},
					yearLabel: {
						formatter: '{start}  1st',
						textStyle: {
							color: '#fff'
						}
					},
					itemStyle: {
						normal: {
							color: '#08304a',
							borderWidth: 1,
							borderColor: '#111'
						}
					}
				}],
				series: [{
//						name: 'TimeLog',
						type: 'scatter',
						coordinateSystem: 'calendar',
						data: me.data,
						symbolSize: function(val) {
							console.log(val[1]/2);
							if(me.unit != 2000) {
								return val[1];
							} else {
								return val[1] / me.unit;
							}
						},
						itemStyle: {
							normal: {
								color: 'rgb(128, 185, 218)'
							}
						}
				}
//					{
//						name: 'Top 12',
//						type: 'effectScatter',
//						coordinateSystem: 'calendar',
//						data: me.data.sort(function(a, b) {
//							return b[1] - a[1];
//						}).slice(0, 12),
//						symbolSize: function(val) {
//							console.log(val[1]/2)
//							if(me.unit != 2000) {
//								return val[1];
//							} else {
//								return val[1] / me.unit;
//							}
//						},
//						showEffectOn: 'render',
//						rippleEffect: {
//							brushType: 'stroke'
//						},
//						hoverAnimation: true,
//						itemStyle: {
//							normal: {
//								color: 'rgb(60, 139, 195)',
//								shadowBlur: 10,
//								shadowColor: '#333'
//							}
//						},
//						zlevel: 1
//					}
				]
			};

			myChart.setOption(option);

			me.$root.Bus.$on('calendar', function(id) {
				////console.log(id);
				$.ajax({
					type: 'get',
					url: '././static/data/calendar.json', //请求数据的地址
					dataType: "json", //返回数据形式为json
					success: function(result) {
						//请求成功时执行该函数内容，result即为服务器返回的json对象
						$.each(result.list, function(index, item) {
							////console.log(item.id)
							if(item.id === id) {
								me.data = item.data
								//console.log(me.data)
								console.log(me.data);
								me.unit = 2;
								myChart.setOption({ //加载数据图表
									series: [{
										data: item.data
									}]
								})
							}
						});
					},
					error: function(errorMsg) {
						//请求失败时执行该函数
						alert("图表请求数据失败!");
					}
				});
			})
		}
	}
</script>

<style>

</style>