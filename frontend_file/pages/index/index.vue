<template>
	<view class="content">
		<view style="height: 100%;">
			<u--image style="font-size: 20% 20%;" src="/static/huanbaolvsebeijing-27756047_1.jpg" mode="widthFix">
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
							placeholder="请输入账号"
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
			<view @click="toweb" style="display: inline-block; width: 160rpx;">
				<navigator url="" hover-class="navigator-hover" style="color: skyblue;text-decoration: underline;">
					忘记密码
				</navigator>
			</view>
			<view @click="toweb" style="display: inline-block; width: 160rpx;">
				<navigator url="" hover-class="navigator-hover" style="color: skyblue;text-decoration: underline;">
					立即注册
				</navigator>
			</view>
		</view>
		<view style="margin-top: 40px; margin-left: 110px;">
			<u-button type="success" :plain="true" text="使用微信一键登录"  shape="circle" @click="wx_login()"> </u-button>
		</view>
	</view>
	
</template>
<script>
	export default {
		data() {
			return {
				userInfo:{},
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {

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
