from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User



@user_bp.route('/')
def get_goods():
    return "get user"

@user_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
        return "有链接"
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        name = data.get("name")
        email = data.get("email")
        number = data.get("number")
        password = data.get("password")
        user_demo = User(name=name, email=email, phone_number=number, password=password)
        sess.add(user_demo)
        sess.commit()
        json_dict = {
            "suc": True,
            "message": "注册成功",
        }
        return jsonify(json_dict)
    return "没有请求格式"
