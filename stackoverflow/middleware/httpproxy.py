from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class ProxyMiddleware(HttpProxyMiddleware):
    """ overwrite process request """

    def process_request(self, request, spider):
        # Set the location of the proxy
        # Using XX-NET port
        proxy_ip = "http://127.0.0.1:8087"
        request.meta['proxy'] = proxy_ip