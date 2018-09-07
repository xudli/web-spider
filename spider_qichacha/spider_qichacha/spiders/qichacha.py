# -*- coding: utf-8 -*-
import scrapy


class QichachaSpider(scrapy.Spider):
    name = 'qichacha'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['http://www.qichacha.com/']

    def parse(self, response):
        pass
