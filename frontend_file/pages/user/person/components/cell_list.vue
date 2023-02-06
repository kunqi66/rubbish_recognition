<template>
	<view class="wrap" v-if="itemList.length > 0">
		<view v-for="(item,index) in itemList" :key="index" @click="handleClick(item)" class="wrap_box"
			:style="{background: item.bg || '#FFF'}">
			<view class="wrap_box_img">
				<u--image :showLoading="true" :src="item.imgSrc" :width="item.imgWidth || '90rpx'"
					:height="item.imgHeight || '90rpx'">
				</u--image>
			</view>
			<view class="wrap_box_list" :style="item.tip ? 'padding-top: 30px' : 'padding-top: 40px'">
				<view class="wrap_box_list_title">{{item.title}}</view>
				<view v-if="item.tip" class="wrap_box_list_tip">
					{{item.tip}}
				</view>
			</view>
			<view class="wrap_box_icon" v-if="iconShow">
				<u-icon :name="item.iName || 'arrow-right'" :color="item.iColor" :size="item.iSize || 28"></u-icon>
			</view>
		</view>
	</view>
</template>

<script>
	/**
	 * itemList => []
	 * @@param {string} title  主标题  
	 * @@param {string} tip    副标题提示  
	 * @@param {string} imgSrc 图片路径  
	 * @@param {string} bg     当前卡片背景色  
	 * @@param {string} imgWidth   图片宽  默认90rpx 
	 * @@param {string} imgHeight  图片高  默认90rpx 
	 * @@param {string} iColor  icon颜色
	 * @@param {string} iName  icon名称  =》 默认角标 arrow-right
	 * @@param {string} iSize  icon大小  =》 默认28
	 * 
	 * @@param {string} iconShow  是否展示icon  默认展示
	 */
	export default {
		name: 'cellList',
		props: {
			itemList: {
				type: Array,
				default: () => []
			},
			iconShow: {
				type: Boolean,
				default: true
			}
		},
		data() {
			return {

			}
		},
		methods: {
			handleClick(e) {
				this.$emit('cellClick', e)
			}
		}
	}
</script>

<style lang="scss" scoped>
	.wrap {
		padding: 0 15px;
		padding-top: 60rpx;

		&_box {
			display: flex;
			margin-bottom: 60rpx;
			height: 210rpx;
			box-shadow: 0px 0px 17px 0px rgba(99, 147, 255, 0.1000);
			border-radius: 40rpx;

			&_img {
				display: flex;
				flex-direction: row;
				align-items: center;
				margin: 0 30rpx;
			}

			&_list {
				flex: 1;

				&_title {
					font-weight: 600;
					font-size: 16px;
					color: #333333;
					padding-bottom: 14rpx;
				}

				&_tip {
					font-size: 14px;
					font-weight: 400;
					color: #999999;
				}
			}

			&_icon {
				width: 80rpx;
				display: flex;
				flex-direction: row;
				align-items: center;
				padding-left: 40rpx;
			}
		}
	}
</style>