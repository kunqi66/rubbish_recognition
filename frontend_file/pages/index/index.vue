<template>
	<view class="content">
		<view style="height: 100%;">
			<u--image style="font-size: 50% 50%;" src="/static/huanbaolvsebeijing-27756047_1.jpg" mode="widthFix">
				 <template v-slot:loading>
					<u-loading-icon color="red"></u-loading-icon>
				  </template>
			</u--image>
		</view>
		<view class="text_home">
			<u--form
							labelPosition="left"
							:model="model1"
							:rules="rules"
							ref="form1"
					>
					<u-form-item
					 label="账号:" prop="userInfo.account" ref="item1">
					<u--input
							placeholder="请输入邮箱"
							prefixIcon="account"
							v-model="model1.userInfo.account"
							prefixIconStyle="font-size: 20px;color: #909399"
						></u--input>
					</u-form-item>
					<u-form-item
					 label="密码:" prop="userInfo.password" ref="item1">
					<u--input
							placeholder="请输入密码"
							prefixIcon="eye"
							type="password"
							v-model="model1.userInfo.password"
							prefixIconStyle="font-size: 20px;color: #909399"
						></u--input>
					</u-form-item>
			</u--form>
		</view>
		
		
		
		<view class="button_home">
			<u-button type="primary" :plain="true" text="登录" @click="login()"></u-button>
			<view @click="resetPasswd()" style="display: inline-block; width: 160rpx;">
				<navigator url="" hover-class="navigator-hover" style="color: skyblue;text-decoration: underline;">
					忘记密码
				</navigator>
			</view>
			<view @click="Register_fun()" style="display: inline-block; width: 160rpx;">
				<navigator url="" hover-class="navigator-hover" style="color: skyblue;text-decoration: underline;">
					立即注册
				</navigator>
			</view>
			<view @click="toManager()" style="display: inline-block; width: 160rpx;">
				<navigator url="" hover-class="navigator-hover" style="color: skyblue;text-decoration: underline;">
					管理员登录
				</navigator>
			</view>
		</view>
		<view style="margin-top: 40px; margin-left: 110px;">
			<u-button type="success" :plain="true" text="使用微信一键登录"  shape="circle" @click="wx_login()"> </u-button>
		</view>
		
		
		
		
		<u-popup :show="register" mode="center" border-radius="14" width="1000rpx" height="6000px" >
			<view style="margin: 50px;">
					<!-- Card start -->
					<uni-card>
						<uni-title type="h1" align="center" title="填写个人信息"></uni-title>
							<u-form :model="registerForm" ref="uForm">
									<u-form-item label="姓名">
											<u-input v-model="registerForm.name" type="text" placeholder="您的昵称" />
									</u-form-item>
									<u-form-item label="邮箱">
											<u-input v-model="registerForm.email" type="text" placeholder="您的昵称" />
									</u-form-item>
									<u-form-item label="电话">
											<u-input v-model="registerForm.number" type="text" placeholder="您的电话" />
									</u-form-item>
									<u-form-item label="密码">
											<u-input v-model="registerForm.password" type="password" placeholder="您的密码" />
									</u-form-item>
									<u-form-item label="确认密码">
											<u-input v-model="registerForm.password1" type="password" placeholder="确认密码" />
									</u-form-item>
								</u-form>
						<view slot="actions" class="card-actions">
							<view class="card-actions-item2">
								<button style="width: 50%;" type="primary" size="mini" @click="submitRegister()">提交</button>
								<button style="width: 50%;" type="primary" size="mini" @click="closeRegister()">关闭</button>
							</view>
						</view>
					</uni-card>
			</view>
		</u-popup>
		
		
		<u-popup :show="resetp" mode="center" border-radius="14" width="1000rpx" height="6000px" >
			<view style="margin: 50px;">
					<!-- Card start -->
					<uni-card>
						<uni-title type="h1" align="center" title="填写个人信息"></uni-title>
							<u-form :model="registerForm" ref="uForm">
									<u-form-item label="邮箱">
											<u-input v-model="registerForm.email" type="text" placeholder="请输入您的注册用邮箱" />
									</u-form-item>
									<u-form-item label="电话">
											<u-input v-model="registerForm.number" type="text" placeholder="输入您的您的电话确认身份" />
									</u-form-item>
									<u-form-item label="密码">
											<u-input v-model="registerForm.password" type="password" placeholder="您的新密码" />
									</u-form-item>
									<u-form-item label="确认密码">
											<u-input v-model="registerForm.password1" type="password" placeholder="确认密码" />
									</u-form-item>
								</u-form>
						<view slot="actions" class="card-actions">
							<view class="card-actions-item2">
								<button style="width: 50%;" type="primary" size="mini" @click="submitReset()">提交</button>
								&nbsp;
								<button style="width: 50%;" type="primary" size="mini" @click="closeReset()">关闭</button>
							</view>
						</view>
					</uni-card>
			</view>
		</u-popup>
		
			<u-toast ref="uToast" />
	
		
		
	</view>
	
	
</template>

<script>
	
	export default {
		data() {
			return {
				paswdshow: false,
				register: false,
				resetp: false,
				registerForm:{},
				resetForm:{},
				userInfo:{},
			}
		},
		onLoad() {

		},
		methods: {
			toManager(){
				uni.navigateTo({
					url:"/pages/Manager/Login"
				})
			},
			showToast() {
				this.$refs.uToast.show({
				title: '登录成功',
				type: 'success',
				url: '/pages/user/index'
							})
			},
			closeRegister(){
				this.register=false;
			},
			closeReset(){
				this.resetp=false;
			},
			resetPasswd(){
				this.resetp=true;
			},
			Register_fun(){
				console.log(this.register)
				this.register=true;
				console.log(this.register)
			},
			submitRegister(){
				var that=this;
				if(that.registerForm.password == that.registerForm.password1){
					console.log("进来发出请求了")
					uni.request({
						header: {'Authorization':getApp().globalData.token,
						   'content-type':'application/x-www-form-urlencoded'},
						url: getApp().globalData.urlRoot+"user/register",
						data:{
							"name": that.registerForm.name,
							"email": that.registerForm.email,
							"number": that.registerForm.number,
							"password": that.registerForm.password,
						},       //json
						method:"POST",
						success: (res) => {
							that.showToast()
							console.log(res)
							console.log(res.data.message)
							if(res.data.suc){
								that.register = false
								that.userInfo.account = that.registerForm.email;
								that.userInfo.password = that.registerForm.password;
								that.login();
							}else{
								console.log(res.data.message)
							}
						},
						fail(){
							console.log("注册失败");
						}
					})
				}else{
					console.log("两次密码输入不一致");
					this.$refs.uToast.show({
							title: '两次密码不一致',
							type: 'error',
							position: 'center',
					})
				}
			},
		}
	}
</script>

<style>
	page{
		background-color: aliceblue;
	}
	.text-home{
		justify-content: center;
		width: 90%;
	}
	.button_home{
		width: 75%;
	}
	.login_button{
			width: 200rpx;
			height: 50rpx;
			display: flex;
			margin-top: 30rpx;
			line-height: 50rpx;
			justify-content: center;
			border-radius: 25px;
			border: 3rpx solid #6699FF;
			font-size: 28rpx;
		}
	.bg-click {
			top: 3upx;
			background-color: #a7a9ff;
		}
	.content {
		background-image: "/static/980.webp";
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: hsl(30, 100%, 50%);
	}
</style>
