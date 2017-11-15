# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
from seospider.database.mysqldb import MysqlDB

class SeospiderPipeline(object):
    def process_item(self, item, spider):
        # with open('data/' + hashlib.md5(item['url']).hexdigest(), 'w') as f:
        #     f.write(item['content'].encode('utf8'))
        sql = "insert into document(url, html) VALUES ('%s', '%s')" % (item['url'], item['html'].replace("'", '"'))
        print(sql)
        MysqlDB.insert(sql)
        return item
