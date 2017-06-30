#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

"""
过滤器和应用不同，在实现过滤器factory的时候，必须要将app参数带入，且必须是第一个位置。
这里过滤器并没有真正过滤什么，实际上应该在__call__中进行一定的处理，设定一定的条件，将一定的条件拦截。
"""

class Boiler(object):
    def __init__(self, app, in_arg):
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Boiler')
        return self.app(environ, start_response)

def filter_app_factory(app, global_config, in_arg):
    return Boiler(app, in_arg)