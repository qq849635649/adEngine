#!/usr/bin/env python
# -*- coding:utf-8 -*-

from decimal import Decimal
import MySQLdb
import Constants

SPACE_SETTLE_PRICE = {}

def connect():
    conn = None
    try:
        conn = MySQLdb.connect(host=Constants.DB_HOST, 
            user=Constants.DB_USERNAME, passwd=Constants.DB_PASSWORD,
            db=Constants.DB_NAME, charset='utf8', read_default_file="/etc/my.cnf", 
            local_infile=1)
    except Exception as e:
        print(e)
        conn = None
    return conn

def syncMySQL():
    conn = connect()
    if conn:
        syncSpacePrice(conn)
    close(conn)

def syncSpacePrice(conn):
    if not conn:
        return

    sql = "SELECT media_id,settle_type,settle_price from media"
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            k = row[0] or 'nokey'
            print k, row[1], row[2]
            SPACE_SETTLE_PRICE[k] = (row[1], row[2])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def close(conn):
    if conn:
        conn.close()

if __name__ == "__main__":
    pass