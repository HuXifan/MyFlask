from flask import Flask, current_app, redirect, url_for, abort
from werkzeug.routing import BaseConverter

# BaseConverter

# Flask类接收一个参数__name__
app = Flask(__name__)  # 当前模块名字, 访问静态资源的url前缀,默认static


# 转换器
# 127.0.0.1/5000/goods/123
@app.route('/goods/<int:goods_id>')  # 不加转换器类型（int，float），默认是不加/的任意普通字符串
def goods_detail(goods_id):
    """定义的视图函数"""

    return 'good_detail page from goods_detail %s' % goods_id, 521


# 1 定义自己的转换器，以类的方式
class RegexConverter(BaseConverter):
    """自定义的转换器"""

    # url_map 放在第一位接受
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)  # Python2
        # super().__init__(url_map)  # python3
        # 将正则表达式的参数保存到对象属性中，flask回去使用这个属性来进行路由的正则匹配
        self.regex = regex  #

    def to_python(self, value):
        print("to_python方法被调用")
        # return "abc"
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        """url_for 的方法的时候被调用"""
        print('to_url方法被调用')
        # return '15956655937'
        return value


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r"1[3456789]\d{9}"


# 2 将自定义的转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter  # 以键值方式保存，不加括号不是创建对象，只是添加类
app.url_map.converters['mobile'] = MobileConverter  # 以键值方式保存，不加括号不是创建对象，只是添加类


@app.route(r'/send/<re(r"1[3456789]\d{9}"):mobile_num>')
# @app.route('/send/<mobile:mobile_num>')
def send_sms(mobile_num):
    return 'page from send_sms  mobile is %s' % mobile_num


@app.route("/index")
def index():
    url = url_for("send_sms", mobile_num='18621125997')
    return redirect(url)


if __name__ == '__main__':
    # app.run()  # 启动flask四程序
    print(app.url_map)  # 通过url_map可以查看整个flask的路由信息
    app.run(debug=True)  # 启动flask四程序,host自定义host主机地址
