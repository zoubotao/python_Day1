#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

from paste import httpserver
# 定义应用程序
def applicaiton(environ, start_response):
    # 设置HTTP的应答状态
    start_response('200 OK', [('Content-type', 'text/html')])
    # 向客户端返回一个字符串
    return ['Hello World\n']
# 启动WSGI服务
"""
第1个参数指定了处理HTTP请求的应用程序（这里的应用程序，通常是指处理HTTP请求的工厂方法。）；
第2个和第3个参数指定了WSGI服务监听的主机和端口。
"""
httpserver.serve(applicaiton, host='127.0.0.1', port=8080)