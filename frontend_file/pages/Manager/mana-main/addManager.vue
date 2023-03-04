<template>
	<view>
		<view  class="form-home">
				<uni-forms ref="form" :modelValue="formData" >
					<uni-forms-item label="姓名" name="name">
						<uni-easyinput prefixIcon="person-filled" type="text" v-model="formData.name" placeholder="请输入昵称">
						</uni-easyinput>
					</uni-forms-item>
					<uni-forms-item label="邮箱" name="email">
						<uni-easyinput prefixIcon="email" type="text" v-model="formData.email" placeholder="请输入邮箱">
						</uni-easyinput>
					</uni-forms-item>
					<uni-forms-item label="电话" name="number">
						<uni-easyinput prefixIcon="phone" type="text" v-model="formData.number" placeholder="请输入电话">
						</uni-easyinput>
					</uni-forms-item>
					<uni-forms-item label="密码" name="password">
						<uni-easyinput prefixIcon="locked" type="password" v-model="formData.password" placeholder="请输入密码">
						</uni-easyinput>
					</uni-forms-item>
					<uni-forms-item label="确认密码" name="password1">
						<uni-easyinput prefixIcon="locked" type="password" v-model="formData.password1" placeholder="请重新输入密码">
						</uni-easyinput>>
					</uni-forms-item>
				</uni-forms>
				<view style="display: flex; margin-left: 10upx;">
				<button class="but" type="primary" @click="submit()">添加</button>
				<button class="but" type="warn" @click="cl()">清空</button>
				</view>
			</view>
	</view>
</template>

<script>
	export default{
		data(){
			return {
				formData:{},
			}
		},
		methods:{
			cl(){
				this.formData.name=""
				this.formData.email=""
				this.formData.number=""
				this.formData.password=""
				this.formData.password1=""
			},
			submit(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/creatManager",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
						"name": that.formData.name,
						"email": that.formData.email,
						"number": that.formData.number,
						"password": that.formData.password,
					},       //json
					method:"POST",
					success(res) {
						if(res.data.suc){
							uni.showToast({
								title: "添加成功！",
								icon: 'checkmarkempty'
							})
							uni.navigateTo({
								url: "/pages/Manager/index",
							})
						}else{
							uni.showToast({
								title: String(res.data.message),
								icon: 'closeempty',
							})
						}
					}
				})
			}
		}
	}
</script>

<style lang="scss">
	.input{
		
	}
	.form-home{
		width: 80%;
		margin-left: 10%;
	}
	.but{
		width: 40%;
		margin: 10upx;
	}
</style>