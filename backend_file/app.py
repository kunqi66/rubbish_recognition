from flask import Flask
import tensorflow as tf
from user.init import user_bp

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(user_bp,url_prefix="/user")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


