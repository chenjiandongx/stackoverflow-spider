#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

UA = UserAgent()


class RandomUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent='Scrapy'):
        super().__init__()
        self.user_agent = user_agent

    def process_request(self, request, spider):
        request.headers.setdefault('Referrer', 'https://stackoverflow.com')
        request.headers.setdefault('User-Agent', UA.random)
