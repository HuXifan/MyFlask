from flask import Flask

app = Flask(__name__)


# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    app.run()  # 启动flask四程序
