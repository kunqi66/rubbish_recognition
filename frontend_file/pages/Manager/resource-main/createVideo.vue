<template>
	<view>
		<view>
			<text class="title">上传视频</text>
		</view>
		<view style="margin-left: 10%; width: 80%; margin-bottom: 20px; margin-top: 20px;">
			<uni-easyinput  type="text" v-model="title" placeholder="请输入视频标题">
			</uni-easyinput>
		</view>
		<view style="margin-bottom: 20px; margin-left: 12%;">
			<video :src="src"></video>
		</view>
		<uni-forms-item label="封面图片">
			<view style="" class="pic" @click="upFile">
				<image style="width: 400rpx;border: aqua solid 1rpx;" v-model="imgurl" :src="imgurl" mode="aspectFit"></image>
			</view>
		</uni-forms-item>
		<view style="margin: auto; width: 80%;">
			<view style="margin-bottom: 20px;">
				<button @tap="upVideo()" type="primary">点我上传视频</button>
			</view>
			<button @tap="submitForm()" type="default">提交</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title:"",
				src:"",
				path:"",
				imgurl:"",
				img_path:"",
			}
		},
		methods: {
			submitForm(){
				console.log("上传了表单");
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/submitVideo",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
							"title": that.title,
							"videourl": that.path,
							"imgurl": that.img_path,
						},
					method:"POST",
					success: (res) => {
						if (res.data.suc) {
							console.log('正常返回')
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}else{
							console.log("上传失败")
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}
					},
				})
			},
			upFile(){
				var that=this;
				uni.chooseImage({
					count: 1,
					sizeType: 'original',
					success: (res) => {
						console.log(res.tempFiles[0]);
						that.imgurl = res.tempFilePaths[0];
						console.log(that.imgurl)
						uni.uploadFile({
									url: getApp().globalData.urlRoot+'manager/upvideoImg', 
									filePath: res.tempFilePaths[0],
									name: 'img',
									header: {'Authorization':getApp().globalData.token},
									success: (uploadFileRes) => {
										console.log(uploadFileRes.data);
										that.img_path=uploadFileRes.data
										console.log("赋值后"+that.img_path)
									}
								});
					},
					error: err=>{
						console.log(err)
					}
				})
			},
			upVideo: function () {
						var self = this;
						var that = this;
						uni.chooseVideo({
							sourceType: ['camera', 'album'],
							success: function (res) {
								self.src = res.tempFilePath;
								uni.uploadFile({
											url: getApp().globalData.urlRoot+'manager/upVideo', 
											filePath: res.tempFilePath,
											name: 'Video',
											header: {'Authorization':getApp().globalData.token},
											success: (uploadFileRes) => {
												console.log(uploadFileRes.data);
												that.path=uploadFileRes.data
												console.log("赋值后"+that.path)
											}
									});
							}
						});
					}
		}
	}
</script>

<style>

</style>
