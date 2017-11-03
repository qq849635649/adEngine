#!/usr/bin/sh python
# -*- coding:utf-8 -*-

import tornado.web

class LogHandler(tornado.web.RequestHandler):
    def initialize(self, **argv):
        self.logType = argv["logType"]
        self.redis = argv["redis"]
        pass

    def get(self):
        self.write("aaaa")
        pass