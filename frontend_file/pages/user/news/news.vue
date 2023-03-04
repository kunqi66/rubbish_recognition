<template>
	<view class="rfeeds">
		<uni-section title="新闻热点" type="line">
					<uni-card padding="0" spacing="0">
						<template v-slot:cover>
							<view class="custom-cover">
								<image class="cover-image" mode="aspectFill" :src="cover">
								</image>
							</view>
						</template>
						<uni-list>
							<uni-list-item  @click="toNews()" v-for="(item,index) in newsList" :key="index" :title="item.title" showArrow></uni-list-item>
						</uni-list>
					</uni-card>
				</uni-section>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				cover: 'https://web-assets.dcloud.net.cn/unidoc/zh/shuijiao.jpg',
				avatar: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png',
				extraIcon:{
						color: '#4cd964',
						size: '22',
						type: 'gear-filled'
				},
				newsList:[],
			
			};
		},
		onLoad() {
			console.log("执行了")
			var that=this;
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"user/newsLoad",
				method:'POST',
				success: (res) => {
					if(res.data.suc){
						console.log("获取视频列表成功")
						that.newsList=res.data.form
						console.log(that.newsList[0].title)
						console.log(that.newsList[0].img_url)
						console.log(that.newsList[0].text)
					}else{
						console.log("未查询到数据")
						console.log(res.data.message)
					}
				},
				fail() {
					uni.showToast({
						title: "获取失败！",
						icon: 'none'
					})
				}
			})
		},
		methods: {
			onClick(e){
							console.log(e)
						},
						actionsClick(text){
							uni.showToast({
								title:text,
								icon:'none'
							})
						}

			
		},
		toNews(){
			console.log("执行了点击")
		}
	};
</script>


<style lang="scss">
	page{
		background-color: aliceblue;
	}
</style>
