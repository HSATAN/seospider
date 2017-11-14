# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SeospiderPipeline(object):
    def process_item(self, item, spider):
        with open('text.txt', 'w') as f:
            f.write(item['content'].encode('utf8'))
        return item
