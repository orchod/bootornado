#!/usr/bin/env python
#coding=utf-8
"""
    bootornado Application
    ~~~~~~~~~~~
    :author: xiao.lin@163.com
"""
import os

import tornado.web
import tornado.locale

from tornado.web import url
from tornado_utils.routes import route

#from pypress import settings as config
from bootornado import uimodules
#from pypress.helpers import setting_from_object
#from pypress.forms import create_forms
from bootornado.views import home,ErrorHandler
#from pypress.database import db, models_committed
#from pypress.extensions.routing import Route
#from pypress.extensions.sessions import RedisSessionStore

class Application(tornado.web.Application):
    def __init__(self):
        handlers = route.get_routes()

        settings = dict(
            title = "bootornado",
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            debug = True,
            ui_modules = uimodules,
            autoescape = None,
            cookie_secret = "bootornado"
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)