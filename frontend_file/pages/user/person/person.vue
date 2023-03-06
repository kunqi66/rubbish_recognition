<template>
	<view>
		<div></div>
		<view style="height: 150px;">
			<button style="background-color:#eef7fe; border: none; size:auto;">
				<view class="image_home">
					<image class="avatar" v-if="managerview == -1" src="/static/logo.png" />
					<image class="avatar" v-if="managerview != -1" src="/static/l.png"></image>
					<view>
					<span style="text-align: center;size: 50px;" >
					<text v-if="managerview == -1" class="img-text">用户昵称</text>
					<text v-if="managerview != -1" class="img-text">微信用户</text>
					</span>
					</view>
				</view>
			</button>
		</view>
		
		<view class="list_home">	
		<uni-list style=" border-radius: 18rpx;">
			<view style="border-radius: 18rpx;">
			<uni-list-item title="个人信息" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
			</view>
			<view>
			<uni-list-item title="修改信息" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
			</view>
			<view>
			<uni-list-item title="个人搜索记录" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
			</view>
			<view>
			<uni-list-item title="新闻观看记录" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
			</view>
		</uni-list>
		</view>
		
		v-bind v-on v-model
		
		<view style="width: 80%; margin-left: 10%; margin-top: 70px;">
			<u-button  v-if="managerview == -1"  type="primary" @click="wx_login()" >用户一键微信登录</u-button>
		</view>
		
		<view style="width: 80%; margin-left: 10%; margin-top: 15px;">
			<u-button  v-if="managerview == -1"  type="primary" @click="mana_login()" >管理员身份认证</u-button>
		</view>
		
		<view style="width: 80%; margin-left: 10%; margin-top: 50px;">
			<u-button  v-if="managerview != -1" type="error"  @click="user_logout()" >退出登录</u-button>
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
		
		
		
		
		
		
		
		
	</view>
	
	
</template>



<script>
	export default {
		data() {
			return {
				logFlag: false,
				openid :'',
				managerview:getApp().globalData.uid,
				paswdshow: false,
				register: false,
				registerForm:{},
				resetForm:{},
				userInfo:{},
			}
		},
		onLoad() {

		},
		methods: {
			closeRegister(){
				this.register=false;
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
							console.log(res)
							console.log(res.data.message)
							if(res.data.suc){
								that.register = false
								that.userInfo.account = that.registerForm.email;
								that.userInfo.password = that.registerForm.password;
								that.wx_login();
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
				}
			},
			
			
			
			
			mana_login(){
				uni.navigateTo({
					url:"/pages/Manager/Login"
				})
			},
			
			
			
			
			
			user_logout(){
				getApp().globalData.uid=-1;
				this.managerview=-1;
			},
			
			
			
			
			
			
			
			wx_login(){
				 var that =this;
				 let wxspAppid = 'wxe73f973f5099f105';
				 let wxspSecret = '07ff2880db69db6936266d1cfa2439ca';
				 let oid= '';
				 uni.login({
				 	provider:'weixin',
				       success(res) {
						uni.getUserInfo({
							provider:'weixin',
							success:function(infoRes){
					   	    that.userInfo = infoRes.userInfo
					    	console.log(that.userInfo)
							}
						});
				         if (res.code) {
				           //发起网络请求
				           uni.request({
				           //这里填你自己的appid 和 wxspSecret 
				             url: "https://api.weixin.qq.com/sns/jscode2session?appid=" + wxspAppid+"&secret=" + wxspSecret + "&js_code=" + res.code + "&grant_type=authorization_code" ,
				             method: "POST",
				             success(res){
				 				oid=res.data.openid
				 				that.openid=oid
				 				uni.request({
				 					header: {'Authorization':"wutoken",
				 								'content-type':'application/x-www-form-urlencoded'},
				 					url: getApp().globalData.urlRoot + "user/Login",
				 					data:{
				 						"oid" :oid,
				 					},
				 					method:"POST",
				 					success: (res1) => {
				 						if(res1.data.suc){
											getApp().globalData.uid=res1.data.uid;
											that.managerview=res1.data.uid;
											uni.showToast({
												title: "登录成功！",
												icon: 'checkmarkempty'
											})
										}
				 					}
				 				})
				 			},
				             fail(data){}
				           })
				         } else {console.log('登录失败！' + res.errMsg)}
				       }
				})
			}
			
		}
	}
</script>

<style lang="scss">
	button::after{
	  border: none;
	}
	page{
		background-color: #eef7fe;
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
	
	//圆形头像
	.avatar{
	    width: 150upx;
	    height: 150upx;
	    border-radius: 50%;
	    // transform: translateY(-50%);
	    margin-top: -75upx;
	}
	.image_home{
		margin-top: 50px;
		margin-left: 20px;
	}
	.img-text{
		padding: 0 10upx;
		color: dimgrey;
		font-size: 20px;
	}
	
	.list_home{
		margin-top: 30px;
  /* 圆角 */
	  border-radius: 80rpx;
	
	  /* 边 */
	  border: 1rpx solid #E0E3DA;
	  /* 阴影 */
	  box-shadow:2rpx 6rpx 0rpx #e5e8df;

		height: auto;
		width: 90%; 
		text-align: center;
		margin-left: 5%;
	}
</style>
