import hashlib
from datetime import datetime

from manager.init import manager_bp
from flask import request,jsonify
from sql_model import sess,Manager
import json
from settings import TOKEN_DIC,UID


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


@manager_bp.route('/Loadmanager',methods=['GET','POST'])
def Loadmanager():
    if request.method == 'POST':
        list = []
        form = sess.query(Manager).all()
        for r in form:
            list.append({
                "name":r.name,
                "email":r.email,
                "number":r.phone_number,
                "id":r.id,
            })
        if form:
            return json.dumps({
                "suc":True,
                "form":list,
            },cls=MyEncoder,indent=4)
        else:
            return json.dumps({
                "suc": False,
                "messager": "未查询到数据",
            })

@manager_bp.route('/editManager',methods=['GET','POST'])
def edit_ma():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()




@manager_bp.route('/creatManager',methods=['GET','POST'])
def creat_ma():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()




# 前端数据 del_id
@manager_bp.route('/deleteManager',methods=['GET','POST'])
def delete_ma():                                          # 等写完添加管理员后测试
    if request.method == "POST":
        if UID == 1:
            form = request.form
            data = form.to_dict()
            del_id = data.get("del_id")
            sess.query(Manager).filter(Manager.id == del_id).delete()
            return json.dumps({
                "suc": True,
                "message": "删除成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "你没有这项权限",
            })


@manager_bp.route('/register',methods=['GET','POST'])    # 得测试
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
        user_demo = Manager(name=name, email=email, phone_number=number, password=password)
        sess.add(user_demo)
        try:
            sess.commit()
        except:
            sess.rollback()
        return json.dumps({
            "suc": True,
            "message": "注册成功",
        })
    return "没有请求格式"


def myhash(str):
    res = hashlib.sha256(str.encode(encoding="utf-8"))
    hash_str = res.hexdigest()
    ans = hash_str[10:30]
    return ans


@manager_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        res = sess.query(Manager).filter(Manager.email == data.get("account")).all()
        if res:
            if res[0].password == data.get("password"):
                now = datetime.now()
                str_now = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
                pre_token = str_now+"{}".format(res[0].id)
                token = myhash(pre_token)
                TOKEN_DIC[token] = res[0].id
                print(TOKEN_DIC)
                return json.dumps({
                    "suc": True,
                    "token": token,
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
                "message": "邮箱未被赋予管理员权限",
            })

