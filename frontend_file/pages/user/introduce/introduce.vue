<template>
	<view class="main">
		<uni-title type="h1" title="垃圾分类标准" color="#2490ff"></uni-title>
		<view class="text-home">
			<text user-select="false" space="nbsp" style="text-indent:30px;">  北京市生活垃圾分为厨余垃圾可回收物、有害垃圾和其他垃圾四类厨余垃圾收集容器是绿色的，可回收物收集容器是蓝色的，有害垃圾收集容器是红色的，其他垃圾收集容器是灰色的。</text>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  北京市生活垃圾处理工作按照“干湿分开，资源回收”，未端决定前先分出厨余垃圾，这样可以避免其他的可回收物被污染，保持厨余垃圾的纯净度，能更有效地进行生化处理;分出可回收物能最大限度地回收资源、循环利用;分出有害垃圾可以杜绝环境污染和对人体健康的伤害;分出其他垃圾能够提高焚烧效率。</text>
		</view>
		
		<image src="/static/introduce/分类.jpg" style="height: 200px; width: 100%;"></image>
		<uni-title type="h1" title="如何投放垃圾" color="#2490ff"></uni-title>
		<view class="text-home">
			<uni-title type="h2" title="厨余垃圾" color="#ffaaa7"></uni-title>
			<image class="img-text" src="/static/introduce/厨余垃圾.png"></image>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  是指家庭中产生的菜帮菜叶、瓜果皮核、剩菜剩饭、废弃食物等易腐性垃圾;从事餐饮经营活动的企业和机关、部队、学校、企业事业等单位集体食堂在食品加工、饮食服务、单位供餐等活动中产生的食物残渣、食品加工废料和废弃食用油脂;以及农贸市场、农产品批发市场产生的蔬菜瓜果垃圾、腐肉、肉碎骨、水产品、畜禽内脏等。其中，废弃食用油脂是指不可再食用的动植物油脂和油水混合物。</text>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  投放要求:厨余垃圾从产生时就应与其他品类垃圾分开，投放前要沥干水分，保证厨余垃圾分出质量，做到“无玻璃陶瓷、无金属杂物、无塑料橡胶”。纯流质的食物垃圾，如牛奶等，应直接倒进下水道。有包装物的过期食品应将包装物去除后分类投放，包装物则投放到对应的可回收物或者其他垃圾收集容器。</text>
		</view>
		<view class="text-home">
			<uni-title type="h2" title="可回收物" color="#ffaaa7"></uni-title>
			<image class="img-text" src="/static/introduce/可回收物.png"></image>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  是指在日常生活中或者为日常生活提供服务的活动中产生的，已经失去原有全部或者部分使用价值，回收后经过再加工可以成为生产原料或者经过整理可以再利用的物品，主要包括废纸类、塑料类、玻璃类、金属类、电子废弃物类、织物类等。</text>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  投放要求:可回收物分类投放时，应尽量保持清洁干燥，避免污染。废纸应保持平整;立体包装物应清空、清洁后压扁投放;玻璃制品应轻投轻放，有尖锐边角的应包裹后投放。</text>
		</view>
		<view class="text-home">
			<uni-title type="h2" title="有害垃圾" color="#ffaaa7"></uni-title>
			<image class="img-text" src="/static/introduce/有害垃圾.png"></image>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  是指生活垃圾中的有毒有害物质。包括废电池(铜镍电池、氧化汞电池、铅蓄电池等 )，废荧光灯管(日光灯管、节能灯等 )废温度计，废血压计，杀虫剂及其包装物，过期药品及其包装物，废油漆、溶剂及其包装物等。</text>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  投放要求:有害垃圾投放应保证器物完整，避免二次污染。锅镍电池、氧化汞电池、铅蓄电池等，投放时应注意轻放;油漆桶、杀虫剂瓶子等,如有残留应密闭后投放;荧光灯、节能灯等易破损物品，应连带包装或包裹后轻放;过期药品应连带包装一并投放。易挥发的有害垃圾，请密封后投放。其余物则投放到对应的可回收物或者其他垃圾收集容器。</text>
		</view>
		<view class="text-home">
			<uni-title type="h2" title="其他垃圾" color="#ffaaa7"></uni-title>
			<image class="img-text" src="/static/introduce/其他垃圾.png"></image>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  指除厨余垃圾、可回收物、有害垃圾之外的生活垃圾以及难以辨识类别的生活垃圾。主要包括餐盒、餐巾纸、湿纸巾、卫生纸、塑料袋、食品包装袋、污染纸张、烟蒂、纸尿裤、一次性餐具、大骨头贝壳、花盆、陶瓷碎片等。简而言之,难以辨识类别的生活垃圾可投入其他垃圾收集容器内。</text>
			<text user-select="false" space="nbsp" style="text-indent:30px;">  投放要求:沥千水分后投放。</text>
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
			
		}
	}
</script>

<style lang="scss">
	page{
		background-color: aliceblue;
	}
	.img-text{
		margin-left: 5%;
		width: 90%;
		height: 150px;
	}
	.main{
		margin: 20upx;
	}
</style>