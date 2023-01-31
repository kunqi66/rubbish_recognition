<template>
			<view class="content">
				<view style="margin:100px;"></view>
				<view class="text_home">
					<u--form
						labelPosition="left"
						:model="userInfo"
						:rules="rules"
						ref="form1"
				>
							<u-form-item
							 label="账号:" prop="userInfo.account" ref="item1">
							<u--input
									placeholder="请输入邮箱"
									prefixIcon="account"
									v-model="userInfo.account"
									prefixIconStyle="font-size: 20px;color: #909399"
								></u--input>
							</u-form-item>
							<u-form-item
							 label="密码:" prop="userInfo.password" ref="item1">
							<u--input
									placeholder="请输入密码"
									prefixIcon="eye"
									type="password"
									v-model="userInfo.password"
									prefixIconStyle="font-size: 20px;color: #909399"
								></u--input>
							</u-form-item>
					</u--form>
				</view>
				
				
				<view class="button_home">
					<u-button type="primary"  text="认证" @click="login()"></u-button>
				</view>
				
			</view>
</template>

<script>
	export default {
		data() {
			return {
				userInfo :{},
			}
		},
		methods: {
			login(){
				var that=this;
				uni.request({
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"manager/Login",
					data:{
						"account": that.userInfo.account,
						"password": that.userInfo.password,
					},       //json
					method:"POST",
					success: (res) => {
						if(res.data.suc){
							console.log(res.data.message)
							uni.navigateTo({
								url:"/pages/Manager/index"
							})
						}else{
							console.log(res.data.message)
						}
					},
					fail() {
						console.log("登陆失败")
					},
					
				})
			},
		}
	}
</script>
<style lang="scss">
	page{
		background-color: bisque;
	}
	.text-home{
		padding-top: 100px;
		margin-top: 100px;
		justify-content: center;
		width: 90%;
	}
	.button_home{
		width: 75%;
	}
	.content {
		background-image: "/static/980.webp";
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>