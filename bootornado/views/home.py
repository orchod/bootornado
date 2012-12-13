#!/usr/bin/env python
#coding=utf-8
"""
    views: blog.py
"""
import simplejson
import logging
import tornado.web
import tornado.escape

from datetime import datetime
from tornado_utils.routes import route

from bootornado.views.base import RequestHandler

@route(r'/', name='index')
class Index(RequestHandler):
    def get(self):
        page_obj = []        
        page_url = None
        self.render("index.html", 
                    page_obj = page_obj,
                    page_url = page_url)
        return