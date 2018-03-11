#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class ProxyMiddleware(HttpProxyMiddleware):

    def __init__(self, proxies):
        self.proxies = proxies

    def process_request(self, request, spider):
        """ 使用外部代理方法 """
        request.meta['proxy'] = self.proxy_shadowsocks()

    @staticmethod
    def proxy_xxnet():
        """ 使用 xx-net 代理 """
        proxy = "http://127.0.0.1:8087"
        return proxy

    @staticmethod
    def proxy_shadowsocks():
        """ 使用 shadowsocks 代理 """
        proxy = "http://127.0.0.1:1080"
        return proxy
