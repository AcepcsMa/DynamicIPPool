# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from scrapy import Request
from IPCrawler.items import ProxyItem

class XiciSpider(scrapy.Spider):
    '''
        Crawler of www.xicidaili.com
    '''
    name = 'Xici'

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    def start_requests(self):
        url = settings["XICI_URL"]
        yield Request(url=url, headers=self.headers)

    def parse(self, response):
        ips = response.xpath("//*[@id='ip_list']/tr[position()>1]/td[2]/text()")
        ports = response.xpath("//*[@id='ip_list']/tr[position()>1]/td[3]/text()")
        types = response.xpath("//*[@id='ip_list']/tr[position()>1]/td[6]/text()")

        for ip, port, type in zip(ips, ports, types):
            proxy = ProxyItem()
            proxy["proxy"] = type.extract() + "#" +ip.extract() + ":" + port.extract()
            yield proxy
