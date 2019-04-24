<template>
	<div id="piechart" style="width: 20%;height: 100%;">
	</div>
</template>

<script>
	import $ from 'jquery'
	import * as echarts from 'echarts'
	export default {
		name: "piechart",
		mounted() {
			var myChart = echarts.init(document.getElementById('piechart'));
			var option = null
			var AgeaName = ['0-17岁', '18～25岁', '26～35岁', '36-60岁', '60岁以上'];
			var ProvinceName = ["四川省", "湖南省", "江西省", "广东省", "青海省", "贵州省", "湖北省", "福建省", "云南省", "辽宁省", "广西壮族自治区", "河南省", "新疆维吾尔自治区", "安徽省", "江苏省", "浙江省", "甘肃省", "山东省", "陕西省", "山西省", "河北省", "黑龙江省", "吉林省", "海南省"];
			var Piedata = [{
					value: 0.7312468951813215,
					name: "四川省"
				},
				{
					value: 0.014903129657228018,
					name: "湖南省"
				},
				{
					value: 0.0024838549428713363,
					name: "江西省"
				},
				{
					value: 0.003477396920019871,
					name: "广东省"
				},
				{
					value: 0.0004967709885742673,
					name: "青海省"
				},
				{
					value: 0.11276701440635867,
					name: "贵州省"
				},
				{
					value: 0.033283656234475906,
					name: "湖北省"
				},
				{
					value: 0.008445106805762544,
					name: "福建省"
				},
				{
					value: 0.027819175360158967,
					name: "云南省"
				},
				{
					value: 0.0009935419771485345,
					name: "辽宁省"
				},
				{
					value: 0.007948335817188276,
					name: "广西壮族自治区"
				},
				{
					value: 0.014903129657228018,
					name: "河南省"
				},
				{
					value: 0.007948335817188276,
					name: "新疆维吾尔自治区"
				},
				{
					value: 0.001987083954297069,
					name: "安徽省"
				},
				{
					value: 0.00546448087431694,
					name: "江苏省"
				},
				{
					value: 0.006954793840039742,
					name: "浙江省"
				},
				{
					value: 0.0009935419771485345,
					name: "甘肃省"
				},
				{
					value: 0.001987083954297069,
					name: "山东省"
				},
				{
					value: 0.00894187779433681,
					name: "陕西省"
				},
				{
					value: 0.0014903129657228018,
					name: "山西省"
				},
				{
					value: 0.0024838549428713363,
					name: "河北省"
				},
				{
					value: 0.0009935419771485345,
					name: "黑龙江省"
				},
				{
					value: 0.0009935419771485345,
					name: "吉林省"
				},
				{
					value: 0.0009935419771485345,
					name: "海南省"
				},
			];
			var agedata = [{
					"四川省": [580, 2, 0, 2, 888, ]
				},
				{
					"湖南省": [30, 0, 0, 0, 0, ]
				},
				{
					"江西省": [5, 0, 0, 0, 0, ]
				},
				{
					"广东省": [7, 0, 0, 0, 0, ]
				},
				{
					"青海省": [1, 0, 0, 0, 0, ]
				},
				{
					"贵州省": [226, 1, 0, 0, 0, ]
				},
				{
					"湖北省": [60, 1, 1, 0, 5, ]
				},
				{
					"福建省": [14, 0, 0, 0, 3, ]
				},
				{
					"云南省": [55, 1, 0, 0, 0, ]
				},
				{
					"辽宁省": [2, 0, 0, 0, 0, ]
				},
				{
					"广西壮族自治区": [16, 0, 0, 0, 0, ]
				},
				{
					"河南省": [26, 1, 0, 0, 3, ]
				},
				{
					"新疆维吾尔自治区": [16, 0, 0, 0, 0, ]
				},
				{
					"安徽省": [4, 0, 0, 0, 0, ]
				},
				{
					"江苏省": [10, 0, 1, 0, 0, ]
				},
				{
					"浙江省": [14, 0, 0, 0, 0, ]
				},
				{
					"甘肃省": [2, 0, 0, 0, 0, ]
				},
				{
					"山东省": [4, 0, 0, 0, 0, ]
				},
				{
					"陕西省": [18, 0, 0, 0, 0, ]
				},
				{
					"山西省": [3, 0, 0, 0, 0, ]
				},
				{
					"河北省": [4, 0, 1, 0, 0, ]
				},
				{
					"黑龙江省": [1, 0, 0, 0, 1, ]
				},
				{
					"吉林省": [1, 1, 0, 0, 0, ]
				},
				{
					"海南省": [0, 0, 0, 0, 2, ]
				}
			]

			var series = [{
				tooltip: {
					trigger: 'item',
					formatter: "{b} : {c} ({d}%)"
				},
				color: ["rgb(200, 220,240)", "rgb(180, 205,230)", "rgb(160, 190,220)", "rgb(140, 175,210)", "rgb(120, 160,200)", "rgb(100, 145,190)", "rgb(80, 130,180)", "rgb(60, 115,170)", "rgb(40, 100,160)", "rgb(20, 85,150)"],
				type: 'pie',
				center: ['40%', '33%'],
				radius: ['20%', '39%'],
				avoidLabelOverlap: false,
				label: {
					normal: {
						show: false,
						position: 'center'
					},
					emphasis: {
						show: true,
						textStyle: {
							fontSize: '20',
							fontWeight: 'bold'
						}
					}
				},
				labelLine: {
					normal: {
						show: false
					}
				},
				data: Piedata
			}]

			for(var i = 0; i < 24; i++) {
				console.log(agedata[i][ProvinceName[i]])
				series.push({
					name: ProvinceName[i],
					type: 'bar',
					stack: '总量',
					data: agedata[i][ProvinceName[i]],
					color: "rgb(" + (200 - i * 20) + ", " + (220 - i * 15) + "," + (240 - i * 10) + ")"
				})

			}
			console.log(series)
			option = {
				tooltip: {
					trigger: 'axis',
					axisPointer: { // 坐标轴指示器，坐标轴触发有效
						type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
					}
				},
				title: [{
					//text: '不同年齡段上网人数（％）',
					left: '30%',
					top: '5%',
					textStyle: {
						color: '#fff'
					}
				}, {
					text: '籍贯上网人数',
					right: '10%',
					top: '5%',
					//textAlign: 'center',
					textStyle: {
						color: '#fff'
					}
				}],
//				legend: {
//					top: "0%",
//					data: ProvinceName,
//					textStyle: {
//						color: '#fff'
//					}
//				},
				grid: {
					left: '3%',
					right: '5%',
					top: '50%',
					bottom: '10%',
					containLabel: true
				},
				xAxis: {
					type: 'value',
					axisLabel: {
						show: true,
						textStyle: {
							color: '#B2B2B2',
							fontSize: 12,
						},
					},
				},
				yAxis: {
					type: 'category',
					data: AgeaName,
					axisLabel: {
						show: true,
						textStyle: {
							color: '#B2B2B2',
							fontSize: 12,
						},
					},
				},
				series: series
			};

			//console.log(option)
			if(option && typeof option === "object") {
				myChart.setOption(option, true);
			}
		}
	}
</script>