import requests
from flask import Flask,request
import tensorflow as tf
from user.init import user_bp
from manager.init import manager_bp
from settings import TOKEN_DIC, UID


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(user_bp,url_prefix="/user")
app.register_blueprint(manager_bp,url_prefix="/manager")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 预处理函数
@app.before_request
def token_verify():
    token = request.headers.get("Authorization")
    print("前端传来的token为{}".format(token))
    if token != "wutoken":
        if token in TOKEN_DIC.keys():
            UID = TOKEN_DIC.get(token)
            print("转化后的uid为{}".format(TOKEN_DIC.get(token)))
        else:
            return "验证身份失败"







if __name__ == '__main__':
    app.run()


