<template>
	<div id="ForignHabits" style="width: 30% height:100%"></div>
</template>

<script>
	import $ from 'jquery'
	import * as echarts from 'echarts'
	import axios from 'axios'
	export default {
		name: "ForignHabits",
		data() {
			return {
				province_01: [],
				province_02: [],
				province_03: [],
				other_provinces: []
			}
		},
		methods: {
			draw() {
				let me=this;
				console.log(document.getElementById('ForignHabits').style.width)
				var myChart = echarts.init(document.getElementById('ForignHabits'));
				var xData = function() {
					var data = [];
					for(var i = 0; i < 24; i++) {
						data.push(i + ":00");
					}
					return data;
				}();

				var  option = {
					// backgroundColor: "#344b58",
					"title": {
						"text": "外来人口上网习惯",
						x: "4%",

						textStyle: {
							color: '#fff',
							fontSize: '18'
						},
						subtextStyle: {
							color: '#90979c',
							fontSize: '16',

						},
					},
					"tooltip": {
						"trigger": "axis",
						"axisPointer": {
							"type": "shadow",
							textStyle: {
								color: "#fff"
							}

						},
					},
					"grid": {
						"borderWidth": 0,
						"top": 110,
						"bottom": 95,
						textStyle: {
							color: "#fff"
						}
					},
					"legend": {
						x: '4%',
						top: '5%',
						textStyle: {
							color: '#90979c',
						},
						"data": ['省份1', '省份2', '省份3', '其他']
					},

					"calculable": true,
					"xAxis": [{
						"type": "category",
						"axisLine": {
							lineStyle: {
								color: '#90979c'
							}
						},
						"splitLine": {
							"show": false
						},
						"axisTick": {
							"show": false
						},
						"splitArea": {
							"show": false
						},
						"axisLabel": {
							"interval": 0,

						},
						"data": xData,
					}],
					"yAxis": [{
						"type": "value",
						"splitLine": {
							"show": false
						},
						"axisLine": {
							lineStyle: {
								color: '#90979c'
							}
						},
						"axisTick": {
							"show": false
						},
						"axisLabel": {
							"interval": 0,

						},
						"splitArea": {
							"show": false
						},

					}],
					"dataZoom": [{
						"show": true,
						"height": 30,
						"xAxisIndex": [
							0
						],
						bottom: 30,
						"start": 0,
						"end": 100,
						handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
						handleSize: '110%',
						handleStyle: {
							color: "#d3dee5",

						},
						textStyle: {
							color: "#fff"
						},
						borderColor: "#90979c"

					}, {
						"type": "inside",
						"show": true,
						"height": 15,
						"start": 1,
						"end": 35
					}],
					"series": [{
							"name": "省份1",
							"type": "bar",
							"stack": "总量",
							"barMaxWidth": 35,
							"barGap": "10%",
							"itemStyle": {
								"normal": {
									"color": "rgba(255,144,128,1)",
									"label": {
										"show": false,
										"textStyle": {
											"color": "#fff"
										},
										"position": "insideTop",
										formatter: function(p) {
											return p.value > 0 ? (p.value) : '';
										}
									}
								}
							},
							"data": me.province_01
						},

						{
							"name": "省份2",
							"type": "bar",
							"stack": "总量",
							"itemStyle": {
								"normal": {
									"color": "rgba(0,191,183,1)",
									"barBorderRadius": 0,
									"label": {
										"show": false,
										"position": "top",
										formatter: function(p) {
											return p.value > 0 ? (p.value) : '';
										}
									}
								}
							},
							"data": me.province_02
						},
						{
							"name": "省份3",
							"type": "bar",
							"stack": "总量",
							"itemStyle": {
								"normal": {
									"color": "rgba(0,191,0,1)",
									"barBorderRadius": 0,
									"label": {
										"show": false,
										"position": "top",
										formatter: function(p) {
											return p.value > 0 ? (p.value) : '';
										}
									}
								}
							},
							data: me.province_03

						},
						{
							"name": "其他",
							"type": "bar",
							"stack": "总量",
							"itemStyle": {
								"normal": {
									"color": "rgba(0,150,0,1)",
									"barBorderRadius": 0,
									"label": {
										"show": false,
										"position": "top",
										formatter: function(p) {
											return p.value > 0 ? (p.value) : '';
										}
									}
								}
							},
							data: me.other_provinces

						}
					]
				}

				myChart.setOption(option);
			}

		},
	mounted() {
		let me=this;
		this.$axios.get('/apis/get_provence_time_point/').then(res => {
			var data = res.data;
			me.province_01 = data[0];
			me.province_02 = data[1];
			me.province_03 = data[2];
			me.other_provinces = data[3];
			me.draw();
		})

	}
	}
</script>

<style>

</style>