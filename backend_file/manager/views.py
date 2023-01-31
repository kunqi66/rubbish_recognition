from manager.init import manager_bp
from flask import request,jsonify
from sql_model import sess,Manager
import json


@manager_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        res = sess.query(Manager).filter(Manager.email == data.get("account")).all()
        if res:
            if res[0].password == data.get("password"):
                return json.dumps({
                    "suc": True,
                    "message": "登录成功",
                })
            else:
                return json.dumps({
                    "suc": False,
                    "message": "密码错误",
                })
        else:
            print("未查询到数据")
            return json.dumps({
                "suc": False,
                "message": "邮箱未注册",
            })

