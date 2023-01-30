from settings import MYSQL_URL


from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker  # 创建连接
from sqlalchemy.ext.declarative import declarative_base   # 创建表的基类

engine = create_engine(
    # //用户名:密码@IP地址:端口/数据库
    MYSQL_URL,
    pool_size=10,  # 连接池大小
    # 超过连接池大小外最多可以创建的连接，也就是一共可以创建15个连接
    max_overflow=5,
    echo=True,  # 调试信息展示
)

Session = sessionmaker(bind=engine)
sess = Session()  # 创建连接  在其他文件使用import导入

Base = declarative_base()

class Host(Base):
    __tablename__ = 'hosts_test'   # 表名
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(126),unique=True,nullable=False)
    port = Column(Integer,default=8080)

class User(Base):
    __tablename__ = 'User'   # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32),nullable=False)
    phone_number = Column(String(32),unique=True,nullable=False)
    email = Column(String(32),unique=True,nullable=False)
    password = Column(String(256),nullable=False)
    wx_token = Column(String(256),nullable=True)


class Manager(Base):
    __tablename__ = 'Manager'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    phone_number = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    face_url = Column(String(64),unique=True,nullable=True)



if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 创建表



    # 主管理员创建信息
    """
    manager_main = Manager(name="kunkun", phone_number="13835678673", email="2839078819@qq.com", password="my123")
    sess.add(manager_main)
    sess.commit()
    """

    # 操作数据库过程示例
    """
    
    Session = sessionmaker(bind=engine)
    sess = Session()  # 创建连接
    # 添加数据
    h = Host(hostname='test1', ip_addr='127.0.0.1')
    h2 = Host(hostname='test2', ip_addr='192.168.1.1', port=8080)
    h3 = Host(hostname='test3', ip_addr='192.168.1.2', port=8081)

    # 添加数据
    sess.add(h)  # 添加一条数据
    sess.add_all([h2, h3])  # 添加多条数据

    # 删除数据
    sess.query(Host).filter(Host.id > 1).delete()

    # 更新数据
    sess.query(Host).filter(Host.id == 1).update({'port': 3309})

    # 查询数据
    # res=sess.query(Host).filter(Host.id==1).all()
    # 查询数据的第二种写法
    res = sess.query(Host).filter_by(id=1).all()
    for r in res:
        print(r.hostname, r.port)

    sess.commit()  # 提交
    """
