# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhiboVideoItem(scrapy.Item):


    title = scrapy.Field()
    video_title=scrapy.Field()
    video_url=scrapy.Field()
  

