<template>
	<view class="content">
		<Search></Search>
			<uni-section title="相关视频" type="line" style="background-color: #eef7fe;">
						<uni-card :cover="cover" @click="onClick(index)"   v-for="(item,index) in videoList"  :key="index">
							 <image slot='cover' style="width: 100%;" :src="cover"></image>
							<text class="uni-body">{{ item.title }}</text>
						</uni-card>
					</uni-section>
					
			<uni-popup ref="video">
				<view style="margin-bottom: 20px; margin-left: 12%;">
					<video :src="src"></video>
				</view>
			</uni-popup>
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
				cover: '',
				videoList:[],
				src:"",
			}
		},
		onLoad(){
			console.log("执行了")
			var that=this;
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"user/videoLoad",
				method:'POST',
				success: (res) => {
					if(res.data.suc){
						console.log("获取视频列表成功")
						that.videoList=res.data.form
						console.log(that.videoList[0].title)
						console.log(that.videoList[0].img_url)
						console.log(that.videoList[0].video_url)
					}else{
						console.log("未查询到数据")
						console.log(res.data.message)
					}
				},
				fail() {
					uni.showToast({
						title: "获取失败！",
						icon: 'none',
					})
				}
			})
		},
		methods: {
			onClick(index){
				console.log("执行了")
				this.src=this.videoList[index].video_url
				this.$refs.video.open()
			}
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
	.prefer-title{
		font-size: 35upx; height: 50upx; line-height: 50upx;
	}
</style>
