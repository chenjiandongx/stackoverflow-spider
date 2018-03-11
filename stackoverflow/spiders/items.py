#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy


class StackoverflowItem(scrapy.Item):

    links = scrapy.Field()
    views = scrapy.Field()
    votes = scrapy.Field()
    answers = scrapy.Field()
    tags = scrapy.Field()
    questions = scrapy.Field()
