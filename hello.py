from flask import Flask

# Flask类接收一个参数__name__
app = Flask(__name__,
            static_url_path='/python',
            static_folder='static', template_folder='templates')  # 当前模块名字, 访问静态资源的url前缀,默认static


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


# 3 直接操作config的字典对象
# app.config['DEBUG'] = True


# import demo
# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
@app.route('/')
def index():
    '''定义的视图函数'''
    # a = 1 / 0
    # 读取配置参数方式
    print(app.config.get('MYNAME'))  # 1 直接从全局对象app的config的字典对象取值  2 通过current_app获取参数

    return 'hello flask'


if __name__ == '__main__':
    # app.run()  # 启动flask四程序
    app.run(host='0.0.0.0', port=5000, debug=True)  # 启动flask四程序,host自定义host主机地址
