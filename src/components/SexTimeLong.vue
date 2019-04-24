<template>
	<div id="SexTimeLong" style="width: 30%;height: 100%;">
	</div>
</template>

<script>
	import $ from 'jquery'
	import axios from 'axios'
	import * as echarts from 'echarts'
	var colors = ["rgb(200, 220,240)", "rgb(160, 190,220)", "rgb(120, 160,200)","rgb(80, 130,180)","rgb(40, 100,160)"];
	export default {
		name: "SexTimeLong",
		data(){
			return{
				man_from_0_to_17: [],
				man_from_18_to_25: [],
				man_from_26_to_35: [],
				man_from_36_to_60: [],
				man_more_than_60: [],
				man_net_bar_01: [],
				man_net_bar_02: [],
				man_net_bar_03: []
			}
		},
		methods:{
			/*from_0_to_17,from_18_to_25,from_26_to_35,from_36_to_60,more_than_60,net_bar_01,net_bar_02,net_bar_03*/
			draw(id,data,title){
				let me = this;
			var xData = function() {
				var data = [];
				for(var i = 0; i < 24; i++) {
					data.push(i);
				}
				return data;
			}();
			
			console.log(document.getElementById(id));
			var myChart=echarts.init(document.getElementById(id));
			
			var  option = {
				//backgroundColor: "#344b58",
				"title": {
					"text": title,
					x: "4%",

					textStyle: {
						color: '#fff',
						fontSize: '16'
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
					"top": 80,
					"bottom": 30,
					textStyle: {
						color: "#fff"
					}
				},
				"legend": {
					x: '4%',
					top: '11%',
					textStyle: {
						color: '#90979c',
					},
					"data": ['0-17', '18-25', '26-35', '36-60', '60+']
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
					"show": false,
					"height": 15,
					"xAxisIndex": [
						0
					],
					bottom: 5,
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
						"name": "0-17",
						"type": "bar",
						"stack": "总量",
						"barMaxWidth": 35,
						"barGap": "10%",
						"itemStyle": {
							"normal": {
								"color": colors[0],
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
						"data": data[0]
					},

					{
						"name": "18-25",
						"type": "bar",
						"stack": "总量",
						"itemStyle": {
							"normal": {
								"color": colors[1],
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
						"data": data[1]
					},
					{
						"name": "26-35",
						"type": "bar",
						"stack": "总量",
						"itemStyle": {
							"normal": {
								"color": colors[2],
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
						"data": data[2]
					},
					{
						"name": "36-60",
						"type": "bar",
						"stack": "总量",
						"itemStyle": {
							"normal": {
								"color": colors[3],
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
						"data": data[3]
					},
					{
						"name": "60+",
						"type": "bar",
						"stack": "总量",
						"itemStyle": {
							"normal": {
								"color": colors[4],
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

						"data": data[4]
					}
				]
			}
				myChart.setOption(option);
			}
		},
		mounted() {
			let me = this;
			
			var wid=$("#SexTimeLong").width();
			var hei=$("#SexTimeLong").height();
			
			var divman=document.createElement("div");
				divman.setAttribute("id","man");
				divman.style.width=wid+"px";
				divman.style.height=hei/2+"px";
			
			var divwoman=document.createElement("div");
				divwoman.setAttribute("id","woman");
				divwoman.style.width=wid+"px";
				divwoman.style.height=hei/2+"px";
			var sexdiv=document.getElementById('SexTimeLong');
			sexdiv.appendChild(divman);
			sexdiv.appendChild(divwoman);
			console.log(sexdiv)
			
			me.$axios.get('/apis/getManAgeAndNetBarHours/').then(res => {
				me.draw('man',res.data,"男性不同年龄上网时长分布");
			})
			
			me.$axios.get('/apis/get_woman_age_and_net_bar_hours/').then(res => {
				//console.log(res.data);
				me.draw('woman',res.data,"女性不同年龄上网时长分布");
			})
		}
	}
</script>

<style>

</style>