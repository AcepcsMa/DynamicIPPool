# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from scrapy import Request
from IPCrawler.items import ProxyItem
import re

class KuaidailiSpider(scrapy.Spider):
    name = 'Kuaidaili'
    # allowed_domains = ['kuaidaili.com']
    # start_urls = ['http://kuaidaili.com/']

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    def start_requests(self):
        url = settings["KUAIDAILI_URL"]
        yield Request(url=url, headers=self.headers)

    def parse(self, response):
        ips = response.xpath("//*[contains(@class, 'table-bordered')]/tbody/tr/td[1]/text()")
        ports = response.xpath("//*[contains(@class, 'table-bordered')]/tbody/tr/td[2]/text()")
        types = response.xpath("//*[contains(@class, 'table-bordered')]/tbody/tr/td[4]/text()")

        for ip, port, type in zip(ips, ports, types):
            proxy = ProxyItem()
            proxy["proxy"] = type.extract() + "#" + ip.extract() + ":" + port.extract()
            yield proxy

        pageCount = int(re.findall("inha/([0-9])/", response.url)[0])
        if pageCount < 3:
            url = re.sub("inha/([0-9])/", "inha/{}/".format(pageCount+1), settings["KUAIDAILI_URL"])
            yield Request(url=url, headers=self.headers)
