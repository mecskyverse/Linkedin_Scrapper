# Scrapy settings for linkedin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'linkedin'
SPIDER_MODULES = ['linkedin.spiders']
NEWSPIDER_MODULE = 'linkedin.spiders'

# HTTPCACHE_ENABLED = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# You can add your api key I have added it here for demo purpose
SCRAPEOPS_API_KEY = 'a18c17ee-0a2d-46b8-9222-aaff27190f44'


SCRAPEOPS_PROXY_ENABLED = True


DOWNLOADER_MIDDLEWARES = {
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1