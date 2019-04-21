# -*- coding: utf-8 -*-

# Scrapy settings for zhibo_video project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhibo_video'

SPIDER_MODULES = ['zhibo_video.spiders']
NEWSPIDER_MODULE = 'zhibo_video.spiders'

ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1,
    #'zhibo_video.pipelines.ZhiboVideoPipeline':1,
#'zhibo_video.pipelines.JsonWithEncodingPipeline':2,
}



#FILES_STORE =""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhibo_video (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#MEMUSAGE_ENABLED=True

#DOWNLOAD_TIMEOUT=30*60
# download_maxsize = 1073741824  #字节
# DOWNLOAD_WARNSIZE=1073741824
# #下载超时
#download_timeout =99999
# MEMUSAGE_ENABLED=True
# MEMUSAGE_LIMIT_MB=0

#FILES_STORE = "F:\\mp4files" #直接使用绝对路径

# #爬虫运行时间
CLOSESPIDER_TIMEOUT = 942221717
DOWNLOAD_MAXSIZE=942221717
#DOWNLOAD_WARNSIZE=335674803
DOWNLOAD_TIMEOUT= 90 * 60


#配置最大并发
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Host': 'cm15-c110-2.play.bokecc.com',
  #  'Host': 'cm15-c110-2.play.bokecc.com',
    'User-Agent': 'okhttp/3.10.0',
  #   'Accept-Language': 'zh,zh-CN;q=0.9',
  # #  'Host': 'www.shengbenbang.cn',
  #   'Connection': 'Keep-Alive',
   # 'Accept-Encoding': 'gzip',
  #   'User-Agent': 'okhttp/3.10.0',
  #
  #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
}
#保存的文件名地址
FEED_URI='zhibo_video.csv'
#保存的格式
FEED_FORMAT = 'csv'
#选择保存的item字段
FEED_EXPORT_FIELDS = ['title', 'video_title', 'video_url']
# FEED_EXPORTERS_BASE = {
# 'json': 'scrapy.exporters.JsonItemExporter',
# 'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
# 'jl': 'scrapy.exporters.JsonLinesItemExporter',
# 'csv': 'scrapy.exporters.CsvItemExporter',
# 'xml': 'scrapy.exporters.XmlItemExporter',
# 'marshal': 'scrapy.exporters.MarshalItemExporter',
# 'pickle': 'scrapy.exporters.PickleItemExporter',
# }
#保存的格式
FEED_EXPORT_ENCODING = 'gbk'

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhibo_video.middlewares.ZhiboVideoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhibo_video.middlewares.ZhiboVideoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
