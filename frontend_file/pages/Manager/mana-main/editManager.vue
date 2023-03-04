<template>
	<view>
		<uni-table ref="table" :loading="loading" border stripe emptyText="暂无更多数据" @selection-change="selectionChange">
						<uni-tr>
							<uni-th width="150" align="center">昵称</uni-th>
							<uni-th width="150" align="center">邮箱</uni-th>
							<uni-th align="center">电话</uni-th>
							<uni-th width="204" align="center">编辑选项</uni-th>
						</uni-tr>
						<uni-tr v-for="(item, index) in tabalDate" :key="index">
							<uni-td>
								<view class="name">{{ tabalDate[index].name }}</view>
							</uni-td>
							<uni-td align="center">{{ tabalDate[index].email }}</uni-td>
							<uni-td align="center">{{ tabalDate[index].number }}</uni-td>
							<uni-td>
								<view class="uni-group">
									<button class="uni-button" size="mini" type="primary" @click="editMmanager(index)">修改</button>
									<button class="uni-button" size="mini" type="warn" @click="deleteManager(index)">删除</button>
								</view>
							</uni-td>
						</uni-tr>
					</uni-table>
					
					
					
		<uni-popup ref="editData">
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
			</uni-forms>
			<view style="display: flex; margin-left: 10upx;">
			<button class="but" type="primary" @click="SubmitEdit()">修改</button>
			<button class="but" type="warn" @click="cl()">清空</button>
			</view>
		</uni-popup>
		
				<view>
					<!-- 提示窗示例 -->
					<uni-popup ref="alertDialog" type="dialog">
						<uni-popup-dialog type="warn" cancelText="关闭" confirmText="同意" title="通知" content="确定要删除该用户吗？" @confirm="submitDelete()"
							@close="dialogClose"></uni-popup-dialog>
					</uni-popup>
				</view>
		
	</view>
</template>

<script>
	export default{
		data(){
			return{
				formData:{},
				edit_id: 0,
				del_id: 0,
				editData:false,
				tabalDate:[],
			}
		},
		onLoad() {
			var that=this
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"manager/Loadmanager",
				method:'POST',
				data:{
					uid:-1,
				},
				success: (res) => {
					if(res.data.suc){
						console.log("获取管理员列表成功")
						that.tabalDate=res.data.form
						console.log(that.tabalDate[0].name)
						console.log(res.data.form)
					}else{
						console.log("未查询到数据")
						console.log(res.data.message)
					}
				},
				fail() {
					uni.showToast({
						title: "获取失败！",
						icon: 'none'
					})
				}
			})
		},
		methods: {
			SubmitEdit(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/editManager",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
						"edit_id": that.edit_id,
						"name":that.formData.name,
						"email" : that.formData.email,
						"number":that.formData.number,
					},       //json
					method:"POST",
					success(res) {
						if(res.data.suc){
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
							uni.navigateTo({
								url: "/pages/Manager/mana-main/editManager",
							})
						}else{
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty',
								duration:1500,
							})
						}
					}
				})
			},
			editMmanager(index){
				this.edit_id=index+1;      
				this.formData.email=this.tabalDate[index].email
				this.formData.number=this.tabalDate[index].number
				this.formData.name=this.tabalDate[index].name
				this.$refs.editData.open()
			},
			deleteManager(index){
				this.del_id=index+1;
				this.$refs.alertDialog.open()
			},
			submitDelete(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/deleteManager",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
						"del_id": that.del_id,
					},       //json
					method:"POST",
					success(res) {
						if(res.data.suc){
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
							uni.navigateTo({
								url: "/pages/Manager/mana-main/editManager",
							})
						}else{
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}
					}
				})
			},
			cl(){
				this.formData.email=""
				this.formData.name=""
				this.formData.number=""
			}
			
		}
	}
</script>

<style lang="scss">
	.uni-group {
		display: flex;
		align-items: center;
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