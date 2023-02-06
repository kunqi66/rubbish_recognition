<template>
	<view class="content">
		<view style="height: 100%;">
			<u--image style="font-size: 50% 50%;" src="/static/huanbaolvsebeijing-27756047_1.jpg" mode="widthFix">
				 <template v-slot:loading>
					<u-loading-icon color="red"></u-loading-icon>
				  </template>
			</u--image>
		</view>
		
		
		
		
		<view class="button_home">
			<u-button type="primary" :plain="true" text="登录" @click="toUser()"></u-button>
		</view>
		
		
	</view>
	
	
</template>

<script>
	
	export default {
		data() {
			return {
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
