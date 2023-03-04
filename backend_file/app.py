import requests
from flask import Flask, request, Response
import tensorflow as tf

import settings
from user.init import user_bp
from manager.init import manager_bp
from settings import TOKEN_DIC
import cv2



app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(user_bp,url_prefix="/user")
app.register_blueprint(manager_bp,url_prefix="/manager")

"""
# VideoCapture可以读取从url、本地视频文件以及本地摄像头的数据
# camera = cv2.VideoCapture('rtsp://admin:admin@172.21.182.12:554/cam/realmonitor?channel=1&subtype=1')
# camera = cv2.VideoCapture('test.mp4')
# 0代表的是第一个本地摄像头，如果有多个的话，依次类推
camera = cv2.VideoCapture('rtsp://admin:admin@192.168.0.101:8081')

def gen_frames():
    while True:
        # 一帧帧循环读取摄像头的数据
        success, frame = camera.read()
        if not success:
            break
        else:
            # 将每一帧的数据进行编码压缩，存放在memory中

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # 使用yield语句，将帧数据作为响应体返回，content-type为image/jpeg
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_start')
def video_start():
    print("进来了")
    # 通过将一帧帧的图像返回，就达到了看视频的目的。multipart/x-mixed-replace是单次的http请求-响应模式，如果网络中断，会导致视频流异常终止，必须重新连接才能恢复
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
"""
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

"""
# 预处理函数
@app.before_request
def token_verify():
    token = request.headers.get("Authorization")
    print("前端传来的token为{}".format(token))
    if token != "wutoken":
        if token in TOKEN_DIC.keys():
            if settings.UID:
                settings.UID[0] = TOKEN_DIC.get(token)
            else:
                settings.UID.append(TOKEN_DIC.get(token))
            print("转化后的uid为{}".format(TOKEN_DIC.get(token)))
        else:
            return "验证身份失败"


"""



if __name__ == '__main__':
    app.run()


