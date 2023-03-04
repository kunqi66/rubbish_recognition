from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User,Video,News
import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


@user_bp.route('/')
def get_goods():
    return "get user"




@user_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        oid = data.get('oid')
        res = sess.query(User).filter(User.wx_token == oid).all()
        if res:
            return json.dumps({
                "suc": True,
                "uid": res[0].id,
            })
        else:
            user_demo = User(wx_token=oid)
            sess.add(user_demo)
            try:
                sess.commit()
            except:
                sess.rollback()
            res = sess.query(User).filter(User.wx_token == oid).all()
            return json.dumps({
                "suc":True,
                "uid":res[0].id,
            })



@user_bp.route('/videoLoad',methods=['GET','POST'])
def videoLoad():
    if request.method == "POST":
        videoList = []
        form = sess.query(Video).all()
        for r in form:
            videoList.append({
                "img_url": r.img_url,
                "video_url": r.url,
                "title": r.title,
            })
        if form:
            return json.dumps({
                "suc":True,
                "form":videoList,
            },cls=MyEncoder,indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })


@user_bp.route('/newsLoad',methods=['GET','POST'])
def newsLoad():
    if request.method == "POST":
        newsList = []
        form = sess.query(News).all()
        for r in form:
            newsList.append({
                "img_url": r.img_url,
                "text": r.text,
                "title": r.title,
            })
        if form:
            return json.dumps({
                "suc":True,
                "form":newsList,
            },cls=MyEncoder,indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })
