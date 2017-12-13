# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import redis

class IpcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class ProxyRedisPipeline(object):
    '''
        Save available proxy to redis
    '''
    def __init__(self):

        # read redis config and build connection pool
        redisHost = settings["REDIS_HOST"]
        redisPort = settings["REDIS_PORT"]
        self.redisPool = redis.ConnectionPool(host=redisHost, port=redisPort)
        self.redisConnect = redis.Redis(connection_pool=self.redisPool)

    def process_item(self, item, spider):

        # save proxy to redis
        self.redisConnect.sadd("proxy", item["proxy"])
        return item