# _*_ coding:utf8: _*_

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from seospider.items import DocmentItem
from scrapy.selector import Selector


class DocmentSpider(CrawlSpider):

    name = 'doc_spider'
    rules = (Rule(link_extractor=LinkExtractor(allow="http://dl.pconline.com.cn/download/358355.html"), callback='parse_item'),)
    start_urls = ['http://dl.pconline.com.cn/download/358355.html']

    def parse_item(self, reponse):

        sel = Selector(reponse)
        item = DocmentItem()
        item['url'] = reponse.url
        item['title'] = ','.join(sel.xpath("//title//text()").extract())
        item['content'] = sel.xpath("//body//text()").extract()
        if item['content']:
            item['content'] = ','.join(set(item['content']))
        print(item)
        return item
