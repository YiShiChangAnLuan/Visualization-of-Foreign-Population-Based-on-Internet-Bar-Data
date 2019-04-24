<template>
	<div id="BarSurfHabits" style="height: 50%;"></div>
</template>

<script>
	import $ from 'jquery'
	import axios from 'axios'
	import * as echarts from 'echarts'
	export default {
		name: 'BarSurfHabits',
		data() {
			return {
				option: {},
				unit:2900
			}
		},
		methods: {
			Init() {
				let me =this;
				var hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
					'7a', '8a', '9a', '10a', '11a',
					'12p', '1p', '2p', '3p', '4p', '5p',
					'6p', '7p', '8p', '9p', '10p', '11p'
				];
				var days = ['0-17', '18-25', '26-35', '36-60', '60+'];

				this.option = {
					title: {
						text: '网吧数据图',
						textStyle:{
							color:"#fff"
						}
					},
					legend: {
						data: ['Punch Card'],
						left: 'right'
					},
					polar: {},
					tooltip: {
						right: 'left',
						formatter: function(params) {
							return days[params.value[0]] + '岁    时间在' + params.value[1] + "到" + (params.value[1] + 1) + '点  有' + params.value[2] + '次开卡记录';
						}
					},
					angleAxis: {
						type: 'category',
						data: hours,
						boundaryGap: false,
						splitLine: {
							show: true,
							lineStyle: {
								color: '#fff',
								type: 'dashed'
							}
						},
						axisLine: {
							show: false
						}
					},
					radiusAxis: {
						type: 'category',
						data: days,
						axisLine: {
							show: false
						},
						axisLabel: {
							rotate: 45
						}
					},
					series: [{
						name: 'Punch Card',
						type: 'scatter',
						color: 'rgb(128, 185, 218)',
						coordinateSystem: 'polar',
						symbolSize: function(val) {
							return val[2]/me.unit;
//							var changeval=Math.log(val[2]);
//							console.log(changeval)
//							if(changeval<7){
//								return changeval;
//							}
//							else if( changeval>=7&& changeval<=9){
//								return changeval*1.1;
//							}
//							else {
//								return changeval*1.5;
//							}
							//return Math.log(val[2]);
						},
						data: []
					}]
				};
			}
		},
		mounted() {
			let me = this;

			//			var wid=$("#habits").height();
			//			var hei=$("#habits").height();
			//			var parentDiv=document.getElementById('habits');
			//			
			//			var barsurfhabits=document.createElement('div');
			//			barsurfhabits.setAttribute("id",'BarSurfHabits');
			//			barsurfhabits.style.width=wid+"px";
			//			barsurfhabits.style.height=hei/2+"px";

			//			var canlendar=document.createElement('div');
			//			canlendar.setAttribute("id",'canlendar');
			//			canlendar.style.width=wid+"px";
			//			canlendar.style.height=hei/2+"px";
			//			
			//			parentDiv.appendChild(barsurfhabits);
			////			parentDiv.appendChild(calendar);

			var mychart = echarts.init(document.getElementById("BarSurfHabits"))
			var data = []
			me.Init();
			click_num("50010000000000")

			function click_num(id) {
				$.ajax({
					type: 'get',
					url: '././static/data/BarSurfHabits.json', //请求数据的地址
					dataType: "json", //返回数据形式为json
					success: function(result) {
						//////console.log(result)
						//请求成功时执行该函数内容，result即为服务器返回的json对象
						$.each(result.list, function(index, item) {
							if(item.id === id) {
								data = item.data
								//console.log(data);
							}
						});
						if(id=="50010000000000")
						{
							me.unit=2900;
						}
						else{
							me.unit=2;
						}
						mychart.hideLoading(); //隐藏加载动画
						
						mychart.setOption({ //加载数据图表
							series: [{
								// 根据名字对应到相应的系列
								data: data
							}]
						});
					},
					error: function(errorMsg) {
						//请求失败时执行该函数
						alert("图表请求数据失败!");
					}
				});
				mychart.setOption(me.option)
			}

			/*网吧id 借口*/
			me.$root.Bus.$on('BarSurfHabits', function(id) {
				click_num(id);
			})
		}
	}
</script>

<style>

</style>