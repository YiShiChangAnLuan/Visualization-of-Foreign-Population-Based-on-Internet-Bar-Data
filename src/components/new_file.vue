<template>
	<div id="app">
		<div class="Inf1">
			<div class="foreignPeople">
				<smallmap class="samllMap"></smallmap>
				<foreignhabits class="ForignHabits"></foreignhabits>
			</div>
			<bigmap  class="BigMap"></bigmap>
			<div class="habits">
				<barsurfhabits class="BarSurfHabits"></barsurfhabits>
				<calendar class="Calendar"></calendar>
			</div>
		</div>
		<div class="Inf2">
			<yichang class="yichang"></yichang>
			<piechart class="piechart"></piechart>
			<sexhabits class="SexHabits"></sexhabits>
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
	import foreignhabits from './components/ForignHabits'
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
			foreignhabits,
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
		height: 50%;
		border: 1px solid #000;
	}
	.Inf1{
		width: 100%;
		height: 50%;
		border: 1px solid #000;
	}
	
	.foreignPeople,
	.habits {
		float: left;
		width: 25%;
		height: 100%;
		border: 1px solid #000;
	}
	
	.BigMap {
		float: left;
		width: 50%;
		height: 100%;
		border: 1px solid #000;
	}
	
	.samllMap,
	.ForignHabits {
		width: 100%;
		height: 50%;
		border: 1px solid #000;
	}
	.piechart,.yichang{
		height: 100%;
		float: left;
	}
	.SexHabits{
		float: left;
	}
</style>