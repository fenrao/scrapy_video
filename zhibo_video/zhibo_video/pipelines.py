# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class ZhiboVideoPipeline(object):
#     def process_item(self, item, spider):
#         return item
import scrapy
import codecs
import json
import time
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class demo(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('file.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        timeSatamp = time.time()
        timeTuple = time.localtime(timeSatamp)
        curTime = time.strftime("%Y-%m-%d %H:%M:%S",timeTuple)
        line = "["+curTime+"] "+json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()


class ZhiboVideoPipeline(FilesPipeline):
    def get_media_requests(self,item,info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url,meta={'title':item['title']})

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no Files")
        item["file_paths"] = file_paths
        return item

    def file_path(self,request,response=None,info=None):
        title = request.meta['title']
        file_guid = title + '.'+request.url.split('/')[-1].split('.')[-1]
        filename = u'{0}'.format(file_guid)
        return filename

