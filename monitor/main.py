#!/usr/bin/sh python
# -*- coding:utf-8 -*-

#tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

# system module
import logging
import os

#own module
from util.Constants import *
from handler.handler import LogHandler

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/log/showLog", LogHandler, dict(logType="show", redis="192.168.1.3:7030")),
        ]
        settings = {'cookie_secret':'geewise', 'gzip':True}
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.options.logging = "WARNING"
    tornado.options.parse_command_line()
    logger = logging.getLogger("tornado_log")
    logger.setLevel(logging.INFO)

    # 
    logger.propagate = False

    if not os.path.exists(TORNADO_LOG_FOLDER):
        os.makedirs(TORNADO_LOG_FOLDER)

    log_file = os.path.join(TORNADO_LOG_FOLDER, 'monitor.%s.log' % (options.port))
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()