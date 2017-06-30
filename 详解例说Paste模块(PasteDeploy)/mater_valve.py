#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Tsou"
# Email:625139905@qq.com

# apt-get install python-paste
# apt-get install python-PasteDeploy

from paste import httpserver
from paste.deploy import loadapp

"""
httpserver在loadapp中将配置文件载入，并绑定到8080端口上。
"""

if __name__ == '__main__':
    httpserver.serve(loadapp('config:congigure.ini', relative_to='.'), host='0.0.0.0', port=8080)

"""
附上另外一种写法，效果相同
from wsgiref.simple_server import make_server
from paste import httpserver
from paste.deploy import loadapp
import os

if __name__ == '__main__':
    configfile = 'configure.ini'
    appname = 'main'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)

    #httpserver.serve(loadapp('config:configure.ini', relative_to = '.'), host = '127.0.0.1', port=8000)

    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()
"""
