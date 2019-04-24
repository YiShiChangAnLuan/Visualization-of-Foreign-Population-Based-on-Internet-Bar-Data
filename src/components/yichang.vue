<template>
	<div id="yichangdiv" style="width: 20%;height: 70%;">
		<Button type="primary" shape="circle" size="small" @click="exportData()" ghost><Icon type="ios-download-outline"></Icon></Button>
		<Table ref="table" :row-class-name="rowClassName" height="TableHight" :data="tableData1" :columns="tableColumns1" @on-row-click="rowClick"></Table>
		<div style="margin: 10px;overflow: hidden">
			<div style="float: right;">
				<Page :total="totalPage" :current="currentPage" :page-size="pageSize" @on-change="changePage"></Page>
			</div>
		</div>
	</div>
</template>
<script>
	import $ from 'jquery'
	import * as d3 from 'd3v4'
	export default {
		data() {
			return {
				TableHight: 300,
				totalPage: 2010,
				currentPage: 1,
				pageSize: 10,
				tableData1: this.changePage(1),
				tableColumns1: [{
						title: '姓名',
						key: 'name'
					},
					{
						title: '年龄',
						key: 'age'
					},
					{
						title: '籍贯',
						key: 'province'
					},
					{
						title: '性别',
						key: 'sex'
					},
					{
						title: '网吧',
						key: 'bar',
						render: (h, params) => {
							return h('Poptip', {
								props: {
									trigger: 'hover',
									title: params.row.bar.length + 'customers',
									placement: 'bottom'
								},
								on: {
									click: () => {
										console.log("test1")
									}
								}
							}, [
								h('Tag', params.row.bar.length),
								h('div', {
									slot: 'content',
									on: {
										click: () => {
											console.log("test2")
										}
									}
								}, [
									h('ul', this.tableData1[params.index].bar.map(item => {
										return h('li', {
											style: {
												textAlign: 'center',
												padding: '4px'
											}
										}, item.n + '：' + item.c)
									}))
								])
							]);
						}
					}
				]
			}
		},
		methods: {
			rowClassName(row, index) {
				if(index % 2 == 0) {
					return 'ivu-table-stripe-even';
				} else return 'ivu-table-stripe-odd';
			},
			exportData(){
				console.log(this.$refs);
				this.$refs.table.exportCsv({
                        filename: 'The Abnormal Personnel Data',
                        data:this.tableColumns1
                });
			},
//			mockTableData1(currentPage) {
//				var me = this;
//				$.ajax({
//					type: 'get',
//					url: '././static/data/yichang.json', //请求数据的地址
//					dataType: "json", //返回数据形式为json
//					success: function(result) {
//						console.log(result)
//						let data = [];
//						for(let i = 0; i < 8; i++) {
//							data.push({
//								name: '黄**',
//								age: Math.floor(Math.random() * 3 + 1),
//								province: "四川",
//								sex: '女',
//								bar: [{
//										n: 'bar1',
//										c: '7890709128'
//									},
//									{
//										n: 'bar2',
//										c: '789079128'
//									},
//									{
//										n: 'bar3',
//										c: '890709128'
//									}
//								],
//							})
//						}
//						me.tableData1 = data;
//					},
//					error: function(errorMsg) {
//						//请求失败时执行该函数
//						alert("图表请求数据失败!");
//					}
//				});
//			},
			formatDate(date) {
				const y = date.getFullYear();
				let m = date.getMonth() + 1;
				m = m < 10 ? '0' + m : m;
				let d = date.getDate();
				d = d < 10 ? ('0' + d) : d;
				return y + '-' + m + '-' + d;
			},
			changePage(currentPage) {
				let me = this;
				$.ajax({
					type: 'get',
					url: '././static/data/teen.json', //请求数据的地址
					dataType: "json", //返回数据形式为json
					success: function(result) {
						console.log(result)
						let data = [];
						var stPage = (currentPage - 1) * me.pageSize;
						for(let i = stPage; i < stPage + me.pageSize; i++) {
							data.push(result[i])
						}
						me.tableData1 = data;
					},
					error: function(errorMsg) {
						//请求失败时执行该函数
						alert("请求数据失败!");
					}
				});
			}
			,
			rowClick(data){
				var bar =data['bar'];
				//console.log(bar)
				var id=[];
				for(var i in bar){
					id.push(bar[i]['c']);
				}
				//console.log(id);
				this.$root.Bus.$emit('yichangBar',id)
			}
		}

	}
</script>

<style>
	.ivu-table-row td {
		color: #fff;
	}
	
	.ivu-table-stripe-even td {
		background-color: #123449;
	}
	/*奇数行*/
	
	.ivu-table-stripe-odd td {
		background-color: #133e5a;
	}
	/*头部 th*/
	
	.ivu-table-header th {
		background-color: #08304a;
		color: #fff;
	}
	/*浮在某行*/
	
	.ivu-table-row-hover td {
		background-color: #08304a;
		color: #000000;
	}
	
	.ivu-table-row-highlight td {
		background-color: #08304a;
	}
</style>