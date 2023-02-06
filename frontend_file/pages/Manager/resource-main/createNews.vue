<template>
	<view>
		<text class="title">编辑新闻</text>
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
				<uni-forms-item label="新闻图片">
					<button @click="upfile()" style="background-color: aliceblue;"><image style="width: 400rpx;border: aqua solid 3rpx;" :src="formData.img" mode="aspectFit">
					</image></button>
				</uni-forms-item>
			</uni-forms>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				formData :{},
			}
		}
	}
</script>

<style>
</style>