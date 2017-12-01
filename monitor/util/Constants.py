#!/usr/bin/sh python
# -*- coding:utf-8 -*-

#http headers
USER_AGENT  = 'User-Agent'
HOST        = 'host'
IP_ADDR     = 'ip'
REAL_IP     = 'X-Real-Ip'
DOMAIN      = 'other'
REFERER     = 'Referer'

# http paramgram
USER_ID     = 'uid'
COST        = 'cost'

# MySQL config
DB_HOST     = '192.168.1.217'
DB_PORT     = 3036
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_NAME     = 'sdk'

#Redis config
REDIS_CONF = "192.168.1.217:7030"

TORNADO_LOG_FOLDER = "/data/monitor/"

BID_EXPIRE_SECOND = 900