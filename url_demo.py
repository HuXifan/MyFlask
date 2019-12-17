from flask import Flask, current_app, redirect, url_for

# Flask类接收一个参数__name__
app = Flask(__name__)  # 当前模块名字, 访问静态资源的url前缀,默认static


# app = Flask('__main__')  # 当前模块名字

# 配置参数使用
# 1 使用配置文件
# app.config.from_pyfile('config.cfg')  # 以文件名指定配置文件
# app.config.from_pyfile('config.cfg')  # 以文件名指定配置文件

# 2使用对象配置
class Config(object):
    DEBUG = True
    MYNAME = 'huxifan'


# 使用对象配置
app.config.from_object(Config)


@app.route('/')
def index():
    '''定义的视图函数'''

    return 'hello flask from index'


# 通过，method限定请求方式
@app.route('/post_only', methods=['get', 'post'])
def post_only():
    # 默认是get请求方式
    return 'post_only page from /post_only'


@app.route('/hello', methods=['post'])
def hello1():
    return 'hello111'


@app.route('/hello', methods=['get'])
def hello2():
    return 'hello222'


@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi  this is Alpha'


@app.route('/login')
def login():
    # url = '/'  # 写死  不好
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for('index')  # 反向推
    return redirect(url)


if __name__ == '__main__':
    # app.run()  # 启动flask四程序
    print(app.url_map)  # 通过url_map可以查看整个flask的路由信息
    app.run(debug=True)  # 启动flask四程序,host自定义host主机地址
