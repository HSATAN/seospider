# _*_ coding: utf8 _*_

import seospider.config.mysql_config as config
import pymysql
import logging


class MysqlDB(object):

    conn = pymysql.connect(host=config.MYSQL_HOST,
                           port=config.MYSQL_PORT,
                           password=config.MYSQL_PASSWORD,
                           db=config.MYSQL_DATABASE,
                           user=config.MYSQL_USER,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()

    @classmethod
    def insert(cls, operation):
        try:
            cls.cursor.execute(operation)
            cls.commit()
        except Exception as e:
            logging.error("insert error: %s" % e)
            cls.rollback()
            cls.commit()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def commit(cls):
        cls.conn.commit()

    @classmethod
    def rollback(cls):
        cls.conn.rollback()