<template>
	<view>
		<text class="title">创建新闻</text>
		<view class="form_home">
			<uni-forms ref="form" :modelValue="formData" >
				<uni-forms-item label="题目">
					<uni-easyinput  type="text" v-model="formData.title" placeholder="请输入新闻标题题目">
					</uni-easyinput>
				</uni-forms-item>
				<uni-forms-item label="正文" style="height: 200px;">
					<uni-easyinput  type="textarea" v-model="formData.text" placeholder="请输入新闻标题题目">
					</uni-easyinput>
				</uni-forms-item>
				
			</uni-forms>
			<uni-forms-item label="新闻图片">
				<view style="" class="pic" @click="upFile" @change="uploadImg">
					<image style="width: 400rpx;border: aqua solid 1rpx;" v-model="imgurl" :src="imgurl" mode="aspectFit"></image>
				</view>
			</uni-forms-item>
		</view>
		<view class="button_home">
			<view style="margin-bottom: 10px;">
				<button type="primary" @click="submitForm()" plain="true">上传推文</button>
			</view>
			<button type="warn" @click="clearForm()" plain="true">重新输入</button>
		</view>
		
	</view>
</template>

<script>
	export default{
		data(){
			return{
				formData :{},
				imgurl:"",
				path:"",
			}
		},
		methods:{
		
			upFile(){
				var that=this;
				uni.chooseImage({
					count: 1,
					sizeType: 'original',
					success: (res) => {
						that.formData.img = res.tempFiles[0];
						console.log(res.tempFiles[0]);
						that.imgurl = res.tempFilePaths[0];
						console.log(that.imgurl)
						uni.uploadFile({
									url: getApp().globalData.urlRoot+'manager/upImg', 
									filePath: res.tempFilePaths[0],
									name: 'img',
									header: {'Authorization':getApp().globalData.token},
									success: (uploadFileRes) => {
										console.log(uploadFileRes.data);
										that.path=uploadFileRes.data
										console.log("赋值后"+that.path)
									}
								});
					},
					error: err=>{
						console.log(err)
					}
				})
			},
			uploadImg(){
				console.log("调用了上传图片");
			},
			submitForm(){
				console.log("上传了表单");
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/submitNews",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
							"title": that.formData.title,
							"text": that.formData.text,
							"path": that.path,
							"uid":-1,
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
			clearForm(){
				console.log("调用了清除表单内容");
				this.formData.title="";
				this.formData.text="";
				this.imgurl="";
			},
		}
	}
</script>

<style>
	.button_home{
		width: 80%;
		padding-left: 10%;
	}
</style>