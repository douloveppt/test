import sys
import uuid

from flask import Flask, request
from flask_script import Manager

# 获取flask对象，括号里初始化基础配置
app = Flask(__name__)


# 定义路由地址：'/'和处理方法hello()
@app.route('/hello/')
def hello_world():
    return 'Hello World'


@app.route('/article/')
def article():
    pk = request.args['pk']
    print(request)
    return '文章详情'


# 路由器匹配规则：<转换器：参数名>
# 转换器：int,string,float,uuid


@app.route('/article/<int:id>/')
def article_detail(id):
    return '文章id为：%s' % id


@app.route('/article/<string:title>/')
def article_title(title):
    return '文章标题为：%s' % title


@app.route('/art_title/<title>/')
def art_title(title):
    return '文章标题为：%s' % title


@app.route('/art_float/<float:price>/')
def art_float(price):
    return '浮点数为：%s' % price


@app.route('/get_uuid/')
def get_uuid():
    a = uuid.uuid4()
    return 'uuid:%s' % str(a)


@app.route('/art_uuid/<uuid:uid>/')
def art_uuid(uid):
    return 'uuid值为：%s' % uid


if __name__ == '__main__':
    # print(sys.argv)
    # host = sys.argv[1]
    # port = sys.argv[2]
    # # 启动flask程序
    # app.run(host=host, port=port, debug=True)
    # flask-script管理启动
    manage = Manager(app)
    manage.run()
