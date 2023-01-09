# vue2学习笔记

## 一、前端知识体系

### 1.1前端三要素

- HTML，内容和结构
- CSS，前端样式
- JavaScript弱类型脚本语言由浏览器直接运行，用于控制网页行为

### 1.2前端MVVM模式

> view--------数据双向绑定--------View Model--------AJAX和JSON-----Model
>
> view（HTML CSS Templates）
>
> View Model（JavaScript  Runtime Compiler）
>
> Model（java业务逻辑层 数据库）

## 二、VUE

### 2.1第一个VUE程序

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <title>第一个vue程序</title>
</head>
<body>
    <div id="app">
        {{message}}
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                message: "Hello Vue!"
            }
        })
    </script>
</body>
</html>
```

> el实现ViewModel和View的绑定
>
> data实现Model和VeiwModel的绑定

### 2.2vue示例生命周期

![生命周期](lifecycle.png)

> 可以后续弄懂

### 2.3vue条件渲染

> v-if只有在条件成立的时候才会把标签渲染到页面上

1. v-if 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回 truthy 值的时候被渲染。

   ```html
   <h1 v-if="awesome">Vue is awesome!</h1>
   ```

2. 也可以用 `v-else` 添加一个“else 块”：

   ```html
   <h1 v-if="awesome">Vue is awesome!</h1>
   <h1 v-else>Oh no 😢</h1>
   ```

3. `v-else-if`，顾名思义，充当 `v-if` 的“else-if 块”，可以连续使用：

   ```html
   <div v-if="type === 'A'">
     A
   </div>
   <div v-else-if="type === 'B'">
     B
   </div>
   <div v-else-if="type === 'C'">
     C
   </div>
   <div v-else>
     Not A/B/C
   </div>
   ```

### 2.4v-show

> 条件显示，标签会渲染到页面中但是是条件显示

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <title>第一个vue程序</title>
</head>

<body>
    <div id="app">
        <h1 v-show="isnum">是手机</h1>
		<h1 v-show="!isnum">不是手机</h1>
		<input type="button" value="fun" v-on:click="fun"/>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                message: "Hello Vue!",
				isnum:true,
            },
			methods:{
				fun: function(){
					this.isnum=!this.isnum;
				}
			}
        })
    </script>
</body>

</html>
```



### 2.5vue列表渲染

> 我们可以用 `v-for` 指令基于一个数组来渲染一个列表。`v-for` 指令需要使用 `item in items` 形式的特殊语法，其中 `items` 是源数据数组，而 `item` 则是被迭代的数组元素的**别名**。

```html
<ul id="example-1">
  <li v-for="item in items" :key="item.message">
    {{ item.message }}
  </li>
</ul>
<script>
var example1 = new Vue({
      el: '#example-1',
      data: {
        items: [
          { message: 'Foo' },
          { message: 'Bar' }
        ]
      }
    })
</script>	
```

v-for的不同实例：

> 对列表循环  对字典循环  对列表套字典循环 循环嵌套

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
		<title>vue列表渲染</title>
	</head>
	<body>
		<div id="app">
			列表循环
			<ul>
				<li v-for="li in list_code">
					{{ li }}
				</li>
			</ul>
			获得索引
			<ol>
				<li v-for="(value,key) in todos">
					{{key}}--{{ value.text }}
				</li>
			</ol>
			循环字典
			<ol>
				<li v-for="value in dictionary">
					value
				</li>
			</ol>
			<ol>
				<li v-for="(value,key) in todoss">
					{{key}}--{{ value.text }} ----
				</li>
			</ol>
		</div>
		
		
		<script>
			var vue=new Vue({
				el:"#app",
				data: {
					list_code:[
						"dasda",
						"dsa",
						"dsadda",
					],
					todos : [
						{ text: '学习神经网络' },
						{ text: "学习vue" },
						{ text: "学习Django" },
						{ text: "学习flask" },
					],
					dictionary:{
						id:2,
						age:23,
						num:"123456",
					},
				}
			})
		</script>
	</body>
</html>
```



### 2.6事件处理

> 可以用 `v-on` 指令监听 DOM 事件，并在触发时运行一些 JavaScript 代码。

```html
<div id="example-1">
  <button v-on:click="counter += 1">Add 1</button>
  <p>The button above has been clicked {{ counter }} times.</p>
</div>
<script>
var example1 = new Vue({
  el: '#example-1',
  data: {
    counter: 0
  }
})
</script>
```

> 然而许多事件处理逻辑会更为复杂，所以直接把 JavaScript 代码写在 `v-on` 指令中是不可行的。因此 `v-on` 还可以接收一个需要调用的方法名称。

```html
<div id="example-2">
  <!-- `greet` 是在下面定义的方法名 -->
  <button v-on:click="greet">Greet</button>
</div>
<script>
    var example2 = new Vue({
      el: '#example-2',
      data: {
        name: 'Vue.js'
      },
      // 在 `methods` 对象中定义方法
      methods: {
        greet: function (event) {
          // `this` 在方法里指向当前 Vue 实例
          alert('Hello ' + this.name + '!')
          // `event` 是原生 DOM 事件
          if (event) {
            alert(event.target.tagName)
          }
        }
      }
    })

    // 也可以用 JavaScript 直接调用方法
    example2.greet() // => 'Hello Vue.js!'
</script>
```

### 2.7表单输入绑定v-model

> 你可以用 `v-model` 指令在表单 `<input>`、`<textarea>` 及 `<select>` 元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。尽管有些神奇，但 `v-model` 本质上不过是语法糖。它负责监听用户的输入事件以更新数据，并对一些极端场景进行一些特殊处理。

v-model使用简单示例

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <title>第一个vue程序</title>
</head>

<body>
    <div id="app">
		<form>
			user:<input type="text" v-model="user"/><br>
			psd:<input type="password" v-model="pwd"/><br>
			<input type="button" value="登录" v-on:click="clickMe"/>
			<input type="button" value="重置" v-on:click="resetform"/>
		</form>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                message: "Hello Vue!",
				user: "",
				pwd: "",
            },
			methods:{
				clickMe :function(){
					console.log(this.user,this.psd)
				},
				resetform:function(){
					this.user="";
					this.pwd="";
				}
			}
        })
    </script>
</body>

</html>
```



### 2.8v-bind绑定

> v-bind为单向绑定，html可以拉取vue中的值 而html中改变不影响vue

v-bind使用实例：

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <title>v_bind使用</title>
	<style>
		.info{
			color: red;
		}
		.danger{
			font-size: 50px;
		}
	</style>
</head>

<body>
	<span> v_bind在动态设置标签属性的时候使用 </span>
    <div id="app">
		{{message}}
		<img alt="" v-bind:src="imgurl" v-bind:class='cls'/>
		<h1 v-bind:class="{info:v1,danger:v2}">测试1</h1> 
		<h1 v-bind:class="clsdic">测试二</h2>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
				imgurl:"static/img/example1.jpg",
                message: "Hello Vue!",
				v1: true,
				v2: true,
				clsdic:{
					info:false,
					danger:true
				}
            }
        })
    </script>
</body>

</html>
```



## 三、Axios实现异步通信

### 3.1什么是Axios

> Axios 是一个基于 *promise* 网络请求库，作用于[`node.js`](https://nodejs.org/) 和浏览器中。 它是 *isomorphic* 的(即同一套代码可以运行在浏览器和node.js中)。在服务端它使用原生 node.js `http` 模块, 而在客户端 (浏览端) 则使用 XMLHttpRequests。

### 3.2Axios安装

> 使用 npm:
>
> ```
> $ npm install axios
> ```
>
> 
>
> 引用：
>
> ```
> <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
> ```
>
> 

### 3.3aixos用例

> 用户登录

```html

```

## 四、组件化开发

### 4.1组件基础

>  组件示例：

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <title>第一个vue程序</title>
</head>

<body>
    <div id="app">
		<button-counter></button-counter>
        {{message}}
    </div>
    <script>
		Vue.component('button-counter', {
		  data: function () {
		    return {
		      count: 0
		    }
		  },
		  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
		})
        var app = new Vue({
            el: "#app",
            data: {
                message: "Hello Vue!"
            },
        })
    </script>
</body>

</html>
```

为了能在模板中使用，这些组件必须先注册以便 Vue 能够识别。这里有两种组件的注册类型：**全局注册**和**局部注册**。至此，我们的组件都只是通过 `Vue.component` 全局注册的.



**通过Prop向子组件传递数据**

> Prop 是你可以在组件上注册的一些自定义 attribute。当一个值传递给一个 prop attribute 的时候，它就变成了那个组件实例的一个 property。为了给博文组件传递一个标题，我们可以用一个 `props` 选项将其包含在该组件可接受的 prop 列表中：

```javascript
Vue.component('blog-post', {
  props: ['title'],
  template: '<h3>{{ title }}</h3>'
})
```

> 一个组件默认可以拥有任意数量的 prop，任何值都可以传递给任何 prop。在上述模板中，我们能够在组件实例中访问这个值，就像访问 `data` 中的值一样。
>
> 一个 prop 被注册之后，你就可以像这样把数据作为一个自定义 attribute 传递进来：

```html
<blog-post title="My journey with Vue"></blog-post>
<blog-post title="Blogging with Vue"></blog-post>
<blog-post title="Why Vue is so fun"></blog-post>
```

> 然而在一个典型的应用中，你可能在 `data` 里有一个的数组：

```javascript
new Vue({
  el: '#blog-post-demo',
  data: {
    posts: [
      { id: 1, title: 'My journey with Vue' },
      { id: 2, title: 'Blogging with Vue' },
      { id: 3, title: 'Why Vue is so fun' }
    ]
  }
})
```

> 并想要为每篇博文渲染一个组件：

```html
<blog-post
  v-for="post in posts"
  v-bind:key="post.id"
  v-bind:title="post.title"
></blog-post>
```



### 4.2局部组件

### 4.3全局组件

> 全局组件示例:

```html

```

