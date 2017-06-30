#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

class DrinkingFountain(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('DringkingFountain')
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'DrinkingFountain')]

def app_factory(global_config, in_arg):
    return DrinkingFountain(in_arg)