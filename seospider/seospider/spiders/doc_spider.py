# _*_ coding:utf8: _*_

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from seospider.items import DocmentItem
from scrapy.selector import Selector
import re


class DocmentSpider(CrawlSpider):

    name = 'doc_spider'
    rules = (Rule(link_extractor=LinkExtractor(), callback='parse_item', follow=True),)
    start_urls = ['http://dl.pconline.com.cn/download/358355.html']

    def parse_item(self, reponse):
        print(dir(reponse))
        sel = Selector(text = self.filter_tags(reponse.text))
        item = DocmentItem()
        item['url'] = reponse.url
        item['title'] = ','.join(sel.xpath("//title//text()").extract())
        item['content'] = sel.xpath("//body//text()").extract()
        if item['content']:
            item['content'] = ','.join(set(item['content'])).replace(' ','')\
                .replace('\n','').replace('\r','').replace('\t','')
        print(reponse.url)
        return item

    def filter_tags(self, htmlstr):
        #  过滤html某些标签
        re_script = re.compile('<script.*?</script>', re.S)  # Script
        re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style

        s = re_script.sub('', htmlstr)  # 去掉SCRIPT
        s = re_style.sub('', s)  # 去掉style
        # 去掉多余的空行
        blank_line = re.compile('\n+')
        s = blank_line.sub('\n', s)
        return s