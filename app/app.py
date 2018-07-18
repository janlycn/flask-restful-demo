
from flask import Flask
from flask_cors import CORS
from lib import configuration, extensions, cli, imports, exception, hooks


app = Flask(__name__)
CORS(app)

# 初始化配置
configuration.init(app)

# 初始化插件
extensions.init(app)

# 导入模块
imports.init(app)

# 初始化cli
cli.init(app)

# 异常
exception.init(app)

# 钩子
hooks.init(app)


if __name__ == '__main__':
    app.run(debug=True)
