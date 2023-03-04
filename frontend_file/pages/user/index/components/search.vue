<template>
	<view>
		<view>
			<text class="search-text">
				可通过文字搜索垃圾种类:
			</text>
			<view class="search-cont">
				<u-search 
				input-align="left" height="35" 
				v-model="keyword" :clearabled="true"
				@search="SubmitSearch()"
				@custom="SubmitSearch()"></u-search>
			</view>
			
			
			<view class="wrap">
						<image src="../../../../static/swiper/封面.jpg" style="height: 180px; width: 100%; margin-top: 20px;"></image>
			</view>
			
			
			
			<view class="lable_home">
					<view class="label-item">	
						<button style="border: 0px; background-color: #eef7fe;">
							<view style="text-align: center;">
							<u-icon name="scan"  color="#b3acc8" size="55"></u-icon>
							</view>
							<view>
							<text>拍照搜索</text>
							</view>
						</button>
					</view>
					<view class="label-item">
					<button style="border: 0px; background-color: #eef7fe;">
						<view style="text-align: center;">
						<u-icon name="mic"  color="#b3acc8" size="55"></u-icon>
						</view>
						<view>
						<text>语音搜索</text>
						</view>
					</button>
					</view>
					<view class="label-item">
					<button style="border: 0px; background-color: #eef7fe;">
						<view style="text-align: center;">
						<u-icon name="file-text"  color="#b3acc8" size="55"></u-icon>
						</view>
						<view>
						<text>垃圾知识</text>
						</view>
					</button>
					</view>
			</view>	
					
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				keyword : "",
				lable:[
					{
						img:'scan',
						title:'拍照搜索',
					},
					{
						img:'mic',
						title:'语音搜索',
					},
					{
						img:'file-text',
						title:'垃圾分类知识',
					}
				],
				}
			},
		}
</script>

<style scoped lang="scss">
	//去除所有button的边框
	button::after{
	  border: none;
	}
	//搜索的css
	.search-cont{
		//disply flex;
		justify-content: space-around;
		height: 70upx;
		align-items: center;
	}
	.search-text{
		padding: 0 10upx;
		color: dimgrey;
	}
	
	//轮播的css
	.wrap {
			padding: 3rpx;
			margin: 0px;
		}
			.swiper {
				height: 300rpx;
			}
			.swiper-item {
				display: block;
				height: 300rpx;
				width: 100%;
				line-height: 300rpx;
				text-align: center;
			}
			
			
			
			
		//lable图标的css
		.label-item{
			width: calc((100%/5)-12px) !important;
			margin: 6px;
			position: relative;
			text-align: center;
		}
		.label-item text{
			font-size: 30upx;
		}
		.lable_home{
			display: flex;
			flex-wrap: wrap;
			align-items: center;
			justify-content: space-between;
			height: 320upx;
			}
		.uploadimg{
			width: 70upx;
			height: 70upx;
			border-radius: 50upx;
			display: block;
			margin: 0 auto;
		}
</style>