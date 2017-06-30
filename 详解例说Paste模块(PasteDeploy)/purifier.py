#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

class Purifier(object):
    def __init__(self, app, in_arg):
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Purifier')
        return self.app(environ, start_response)

def filter_app_factory(app, global_conf, in_arg):
    return Purifier(app, in_arg)