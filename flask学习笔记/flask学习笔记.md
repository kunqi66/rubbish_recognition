# Flask学习笔记

## 一、Flask工程搭建和配置

### 1.1flask的hello world

可以直接创建例如helloworld.py文件一样的一个普通的python文件

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

启动运行：

```
python helloworld.py
```

### 1.2参数说明

1. Flask对象初始化参数

   ```
   1.import_name Flask所在的包，传__name__就可以
   2.static_url_path 静态文件访问路径，可以不传，默认为：/+static_folder
   3.static_folder  默认为static
   4.templates_folder  默认为templates
   ```

   

2. 应用程序配置参数

   Flask所有的配置信息都保存在app.config属性里面，该属性可以按照字典方式进行操作
   读取：

    * app.config.get(name)
    * app.config[name]

   设置：

   * 从配置对象中加载

     app.config.from_object(配置对象)

     ```python
     class DefaultConfig(object):  #配置写在类中
         """默认配置"""
         SECRET_KEY='sdadada'
     app = Flask(__name__)
     app.config.from_object(DefaultConfig)
     ```

   * 从配置文件中加载

     新建一个setting.py

     ```python
     SECRT_KEY='dasasdasdas'
     ```

     在Flask文件中：

     ```python
     app=Flask(__name__)
     app.config.from_pyfile('setting.py')
     ```

   * 从环境变量中加载

     ```python
     app.config.from_envvar('环境变量名',silent=True)
     # 环境变量的值为一个配置文件
     ```

     

3. app.run()运行参数

> host   运行ip    port  运行端口 app.run(host="",port=,deBug=True)

直接运行Flask项目：

```
flask run
环境变量 FLASK_APP 指明flask启动实例
flask run -h 0.0.0.0 -p 8000 指定主机和端口运行
flask run --help 获取帮助
环境变量FLASK_ENV决定生产模式和开发模式
development
production
```



## 二、路由和蓝图

### 1.1查询路由

使用命令直接查询当前app所有路由

```cmd
flask routes
```

在代码中查找路由

```python
app = Flask(__name__)
print(app.url_map)
```

使用例子

构造获取全部路由信息的接口：

```python
#需求，需要遍历一个url_map  取出特定信息 在一个特定的接口返回


```

### 1.2flask请求方式

1. GET
2. OPTION（自带） 简化版的GET请求 用于询问服务器接口信息的
3. HEAD（自带） 简化版GET请求 只返回响应头不返回响应体

以上三种为默认支持的请求方式

自定请求方式使用methods参数

```python
@app.route("/",methods=["POST","GET"])
```



 ### 1.3蓝图的定义使用

在Flask当中使用蓝图来对模块进行组织管理，可以视为存储一组视图方法的容器对象

每一个蓝图有自己的模板静态文件可以独立定义url前缀

在初始化一个应用时，就应该注册需要使用的蓝图

使用蓝图的三个步骤：

1. 创建一个蓝图对象

   ```python
   user_bp=Blueprint('user',__name__)# 相当于app=Flask(__name__)参数也一样 没有默认的static了
   ```

   

2. 在这个蓝图对象上进行操作，注册路由，指定静态文件夹，注册模板过滤器

   ```python
   @user_bp.router('/')
   def user_profile(): 
       return 'user_profile'
   ```

   

3. 在应用对象上注册这个蓝图

   ```python
   app.register_blueprint(user_bp,url_prefix="/user") #加url前缀
   ```

在目录中创建蓝图

新建一个目录

在init中

```python
from flask import Blueprint

good_bp=Blueprint('goods',__name__)

from . import views
```

新建views.py文件

```python
from . import goods_bp

@goods_bp.route('goods')
def get_goods():
    return 'get goods'
```

在app文件中

```python
import goods import goods_bp
app.register_blueprint(goods_bp)
```



## 三、请求和响应

