import hashlib
from datetime import datetime
import os
from manager.init import manager_bp
from flask import request,jsonify
from sql_model import sess,Manager,News,Video
import json
from settings import TOKEN_DIC,UID,cur_path



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
                "message": "未查询到数据",
            })

@manager_bp.route('/editManager',methods=['GET','POST'])
def edit_ma():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        id = data.get("edit_id")
        res =sess.query(Manager).filter(Manager.id == id).all()
        if res:
            res[0].email = data.get("email")
            res[0].phone_number = data.get("number")
            res[0].name = data.get("name")
            return json.dumps({
                "suc": True,
                "message": "修改成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })



@manager_bp.route('/creatManager',methods=['GET','POST'])
def creat_ma():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        name = data.get("name")
        email = data.get("email")
        res = sess.query(Manager).filter(Manager.email == email).all()
        res = list(res)
        print("这是查找到的{}".format(res))
        if res:
            return json.dumps({
                "suc": False,
                "message": "邮箱已注册为管理员",
            })
        number = data.get("number")
        res = sess.query(Manager).filter(Manager.phone_number == number).all()
        res = list(res)
        if res:
            return json.dumps({
                "suc": False,
                "message": "电话已注册为管理员",
            })
        password = data.get("password")
        if password and number and email and name:
            user_demo = Manager(name=name, email=email, phone_number=number, password=password)
            sess.add(user_demo)
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "创建成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "输入信息不全",
            })
    return "没有请求格式"



# 前端数据 del_id
@manager_bp.route('/deleteManager',methods=['GET','POST'])
def delete_ma():                                          # 等写完添加管理员后测试
    if request.method == "POST":
        print(UID[0])
        if UID[0] == 1:
            form = request.form
            data = form.to_dict()
            del_id = data.get("del_id")
            sess.query(Manager).filter(Manager.id == del_id).delete()
            try:
                sess.commit()
            except:
                sess.rollback()
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
    now = datetime.now()
    str_now = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    str += str_now
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


@manager_bp.route('/upImg',methods=['GET','POST'])
def upImg():
    if request.method == 'POST':
        imgData = request.files['img']
        imgName = myhash(imgData.filename)
        print(imgName)
        imgName = imgName+'.jpg'
        UPLOAD_FOLDER = 'static\\frontend_img\\news_img'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        path = os.path.join(file_dir, imgName)
        imgData.save(path)
        return path



@manager_bp.route('/upvideoImg',methods=['GET','POST'])
def upvideoImg():
    if request.method == 'POST':
        imgData = request.files['img']
        imgName = myhash(imgData.filename)
        print(imgName)
        imgName = imgName+'.jpg'
        UPLOAD_FOLDER = 'static\\frontend_img\\video_img'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        path = os.path.join(file_dir, imgName)
        imgData.save(path)
        return path


@manager_bp.route('/upVideo',methods=['GET','POST'])
def upVideo():
    if request.method == 'POST':
        videoDate = request.files['Video']
        videoName = myhash(videoDate.filename)
        print(videoName)
        videoName = videoName+'.mp4'
        UPLOAD_FOLDER = 'static\\frontend_img\\video'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        path = os.path.join(file_dir, videoName)
        videoDate.save(path)
        return path





@manager_bp.route('/submitNews',methods=['GET','POST'])
def submitNews():
    if request.method == 'POST':
        print("执行")
        form = request.form
        data = form.to_dict()
        title = data.get("title")
        text = data.get("text")
        print("提取")
        path = data.get("path")
        message = News(title=title,text=text,img_url=path)
        sess.add(message)
        try:
            sess.commit()
            print("保存成功")
            return json.dumps({
                "suc": True,
                "message": "上传成功",
            })
        except:
            sess.rollback()
            return json.dumps({
                "suc":False,
                "message":"上传失败",
            })


@manager_bp.route('/submitVideo',methods=['GET','POST'])
def submitVideo():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        title = data.get("title")
        url = data.get("videourl")
        imgurl = data.get("imgurl")
        message = Video(title=title, url=url, img_url=imgurl)
        sess.add(message)
        try:
            sess.commit()
            print("保存成功")
            return json.dumps({
                "suc": True,
                "message": "上传成功",
            })
        except:
            sess.rollback()
            return json.dumps({
                "suc": False,
                "message": "上传失败",
            })

