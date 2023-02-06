from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User
import json


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

