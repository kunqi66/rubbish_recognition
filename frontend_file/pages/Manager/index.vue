<template>
	<view>
		<view style="margin-left: 45rpx;color: orange;margin-top: 30rpx;font-size: 20px;">
			<text>管理员选项</text>
		</view>
		
		<view class="card-home">
			<view style="margin-left: 20rpx;margin-bottom: 10rpx; font-size: 15px;">
				<text>用户管理</text>
			</view>
			<uni-card>
				<uni-list style=" border-radius: 18rpx;">
					<view style="border-radius: 18rpx;">
					<uni-list-item title="增加管理员" link to="/pages/Manager/mana-main/addManager" @click="onClick($event,1)"></uni-list-item>
					</view>
					<view>
						<uni-list-item title="编辑管理员" link to="/pages/Manager/mana-main/editManager" @click="onClick($event,1)"></uni-list-item>
					</view>
					
				</uni-list>
			</uni-card>
		</view>
		
		<view class="card-home">
			<view style="margin-left: 20rpx;margin-bottom: 10rpx;font-size: 15px;">
				<text>资源管理</text>
			</view>
			<uni-card>
				<uni-list style=" border-radius: 18rpx;">
					<view style="border-radius: 18rpx;">
					<uni-list-item title="新建新闻" link to="/pages/Manager/resource-main/createNews" @click="onClick($event,1)" ></uni-list-item>
					</view>
					<view>
					<uni-list-item title="编辑新闻" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
					</view>
					<view>
					<uni-list-item title="新建推文" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
					</view>
					<view>
					<uni-list-item title="编辑推文" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
					</view>
					<view>
					<uni-list-item title="新建答题" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
					</view>
					<view>
					<uni-list-item title="修改答题" link to="/pages/vue/index/index" @click="onClick($event,1)" ></uni-list-item>
					</view>
				</uni-list>
			</uni-card>
		</view>
		<view style="margin: 30px;">
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			onclick(u,number){
				uni.navigateTo({
					url: u
				})
			},
		}
	}
</script>

<style>
	.card-home{
		margin-top: 40px;
	}
	.item_button{
		width: 100%;
		height: 15px;
	}
</style>
