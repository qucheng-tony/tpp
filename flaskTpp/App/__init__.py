from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.apis import init_api


def init_app(env):
    app=Flask(__name__)
    #设置文件
    app.config.from_object(envs.get(env))
    #设置扩展库
    init_ext(app)
    #设置views,apis
    init_api(app)

    return app