# -*- coding: utf-8 -*-


BOT_NAME = 'stackoverflow'

SPIDER_MODULES = ['stackoverflow.spiders']
NEWSPIDER_MODULE = 'stackoverflow.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# encoding setting
FEED_EXPORT_ENCODING = 'utf-8'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Maximum number of concurrent items (per response) to process in parallel in the Item Processor(defalut:100)
CONCURRENT_ITEMS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# his setting is also affected by the RANDOMIZE_DOWNLOAD_DELAY setting (which is enabled by default).
# By default, Scrapy doesn’t wait a fixed amount of time between requests,
# but uses a random interval between 0.5 * DOWNLOAD_DELAY and 1.5 * DOWNLOAD_DELAY.
DOWNLOAD_DELAY = 4


# The download delay setting will honor only one of:
# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain (defalut:8)
CONCURRENT_REQUESTS_PER_DOMAIN = 16

# The maximum limit for Twisted Reactor thread pool size. (defalut:10)
REACTOR_THREADPOOL_MAXSIZE = 32

# Defines the maximum times a request can be redirected. (deaflut:20)
# After this maximum the request’s response is returned as is. We used Firefox default value for the same task.
# REDIRECT_MAX_TIMES = 25

# Retrying failed HTTP requests can slow down the crawls substantially,
# specially when sites causes are very slow (or fail) to respond,
# thus causing a timeout error which gets retried many times,
# unnecessarily, preventing crawler capacity to be reused for other domains.
REDIRECT_ENABLED = False

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enables the AutoThrottle extension.(default:Flase)
AUTOTHROTTLE_ENABLED = False

# The amount of time (in secs) that the downloader will wait before timing out.(defalut:180)
# Unless you are crawling from a very slow connection (which shouldn’t be the case for broad crawls)
# reduce the download timeout so that stuck requests are discarded quickly and
# free up capacity to process the next ones.
# recommend : DOWNLOAD_TIMEOUT = 15
DOWNLOAD_TIMEOUT = 120


# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'stackoverflow.middlewares.StackoverflowSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# from stackoverflow.spiders.stackoverflow_spider import StackoverflowSpider
DOWNLOADER_MIDDLEWARES = {
   'stackoverflow.middleware.useragent.RandomUserAgentMiddleware': 400,
   # 'stackoverflow.middleware.httpproxy.ProxyMiddleware': 750,
}
