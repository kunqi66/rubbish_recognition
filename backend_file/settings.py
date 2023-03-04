import os
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/rubbish_bs'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 项目相关全局变量配置
MYSQL_URL = 'mysql+pymysql://root:123456@127.0.0.1:3306/rubbish_bs'
TOKEN_DIC = {}

UID = []
# 获取当前文件的目录
cur_path = os.path.abspath(os.path.dirname(__file__))
