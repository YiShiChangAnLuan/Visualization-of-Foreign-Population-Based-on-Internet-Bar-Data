<template>
	<div id="app">
		<div class="Inf1">
			<div class="habits">
				<barsurfhabits class="BarSurfHabits"></barsurfhabits>
				<calendar class="Calendar"></calendar>
			</div>
			<bigmap  class="BigMap"></bigmap>
			<smallmap class="samllMap"></smallmap>
		</div>
		<div class="Inf2">
			<sexhabits class="SexHabits"></sexhabits>
			<yichang class="yichang"></yichang>
			<piechart class="piechart"></piechart>
			<SexTimeLong class="sextimelong"></SexTimeLong>
		</div>
	</div>
</template>
<script>
	import * as d3 from 'd3v4'
	import smallmap from './components/smallMap'
	import yichang from './components/yichang'
	import piechart from './components/piechart'
	import barsurfhabits from './components/BarSurfHabits'
	import calendar from './components/calendar'
	import bigmap from './components/BigMap'
	// 修改外来人口上网习惯到男女时长  ForignHabits -> SexHabitsSave 
	//import foreignhabits from './components/ForignHabits'
	import SexTimeLong from './components/SexTimeLong'
	import sexhabits from './components/SexHabits'
	
	export default {
		name: 'App',
		components: {
			smallmap: smallmap,
			yichang:yichang,
			piechart,
			barsurfhabits,
			calendar,
			bigmap,
			SexTimeLong,
			sexhabits
		},
		data() {
			return {
			}
		},
		mounted(){
			/*var Inf2=document.getElementById("Inf2");
			console.log(Inf2)
			Inf2.style.height=document.querySelector(".Inf1").style.height;
			console.log(Inf2.style.height)*/
		}
	}
</script>

<style>
	html,body,#app{
		width: 100%;
		height: 100%;
		background-color:#08304a;
	}
	
	.Inf2{
		width: 100%;
		height: 60%;
		/*border: 1px solid #000;*/
	}
	.Inf1{
		width: 100%;
		height: 40%;
		/*border: 1px solid #000;*/
	}
	
	.habits,.BigMap,.samllMap{
		float: left;
	}
	.habits{
		width: 25%;
		height: 100%;
	}
	.samllMap{
		width: 25%;
		height: 100%;
	}
	.sextimelong{
		width: 25%;
		height: 100%;
		float: right;
	}
	.SexHabits,.yichang,.piechart{
		float: left;
	}
	
</style>