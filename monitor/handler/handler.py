#!/usr/bin/sh python
# -*- coding:utf-8 -*-

import tornado.web
import time,urllib

from util.Constants import *
from util import Constants

class LogHandler(tornado.web.RequestHandler):
    def initialize(self, **argv):
        self.logType = argv["logType"]
        self.redis = argv["redis"]
        pass

    def get(self):
        print "get a new request"

        self.set_header("Content-Type", "text/html")
        self.set_header("Access-Control-Allow-Origin", "*")

        if self.logType == "page":
            self.bid = "no_bid"
            self.safeLogAd()
            return

        self.bid = self.get_argument('bid', None)
        if not self.bid:
            self.jump()
            return

        ad_timestamp = self.get_argument("ts", int(time.time()))
        cur_timestamp = int(time.time())
        if not ad_timestamp or (cur_timestamp - ad_timestamp) > BID_EXPIRE_SECOND:
            self.jump()
            return

        print "aa"
        if self.logType in ("show", "click", "video"):
            self.safeLogAd()
            return
        else:
            self.jump()
            return

        
    def safeLogAd(self):
        print "safeLogAd"

        ip_addr = (REAL_IP in self.request.headers and self.request.headers[REAL_IP]) or self.request.remote_ip or self.get_argument("IP_ADDR", default=None)
        ua = USER_AGENT in self.request.headers and self.request.headers[USER_AGENT]
        
        if len(ua) < 20:
            self.jump()
            return

        uid = self.get_argument("uid", "")
        dspId = self.get_argument("dspid", "")
        #dspId = urllib.unquote(str(dspId))
        pid = self.get_argument("pub", default=None)
        if not pid:
            pid = self.get_argument("pid", default=None)
        if not pid or pid == "undefined" or len(pid) != 32:
            self.jump()
            return

        space_id = self.get_argument("spaceid", "")
        area_id = self.get_argument("cc", "")
        ctype = self.get_argument("ctype", default='1')
        isPC = self.get_argument("isPC", default='1')
        platform = self.tran_platform()

        adSrc = self.get_argument("src", "")
        if not adSrc and dspId:
            if 'geewise' in dspId or 'batmobi' in dspId:
                adSrc = "rtb"
            else:
                adSrc = 'union'

        self.jump()

    def jump(self):
        print "send a response"
        return self.write("OK")

    def tran_platform():
        pass
