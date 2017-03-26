# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class StackoverflowItem(scrapy.Item):

    links = scrapy.Field()
    views = scrapy.Field()
    votes = scrapy.Field()
    answers = scrapy.Field()
    tags = scrapy.Field()
    questions = scrapy.Field()
