#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

"""
应用里面的结构是类似的，需要注意的factory方法的参数，这与filter的factory有所不同。
每一个应用类内部的__init__和__call__方法是需要自己实现的，__call__方法返回的字符串将显示在web界面上，
start_response(status, response_headers)语句及其参数涉及到wsgi需要了解。
"""

class Tap(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Tap')
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Tap')]

def app_factory(global_config, in_arg):
    return Tap(in_arg)