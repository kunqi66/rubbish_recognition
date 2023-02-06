<template>
	<view class="content">
		<Search></Search>
		<Context></Context>
	</view>
</template>

<script>
	import Search from './components/search.vue'
	import Context from './components/context.vue'
	import Title from './components/title.vue'
	
	export default {
		components: {
			Search,
			Context,
			Title,
		},
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style lang="scss">
	page{
		background-color: #eef7fe;
	}
	.content{
		margin: 0 20upx;     //整体的一个边界
	}
</style>
