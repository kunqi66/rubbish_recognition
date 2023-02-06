<script>
	export default {
		globalData: {
			uid : -1,
			urlRoot: "http://127.0.0.1:5000/",
			token:"wutoken",
		},
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
	/*每个页面公共css */
	@import "uni_modules/uview-ui/index.scss";
	@import "uni_modules/uview-ui/theme.scss";
	page{
		background-color: #eef7fe;
	}
</style>


