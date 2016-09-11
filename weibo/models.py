from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time

# 以下都是套路
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 指定数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weibos.db'

db = SQLAlchemy(app)


class ModelHelper(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# 定义一个 Model，继承自 db.Model
class Weibo(db.Model, ModelHelper):
    __tablename__ = 'weibos'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String(), default='')

    # 定义关系
    user_id = db.Column(db.Integer)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.username = form.get('username', '')
        self.comments = []

    def load_comments(self):
        self.comments = Weibo_Comment.query.filter_by(weibo_id=self.id).all()


class Weibo_Comment(db.Model, ModelHelper):
    """
    评论微博
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    create_time = db.Column(db.Integer, default=0)
    username = db.Column(db.String(), default='')

    # 定义关系
    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)

    def __init__(self, form):
        self.comment = form.get('comment', '')
        self.created_time = int(time.time())
        self.username = form.get('username', '')


def init_db():
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')


if __name__ == '__main__':
    init_db()