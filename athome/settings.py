# -*- coding: utf-8 -*-

# Scrapy settings for athome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'athome'

SPIDER_MODULES = ['athome.spiders']
NEWSPIDER_MODULE = 'athome.spiders'

LOG_LEVEL = 'INFO'
LOG_FORMATTER = 'athome.logging.polite.PoliteLogFormatter'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'athome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'athome.middlewares.AthomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'athome.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'athome.pipelines.becloud.DuplicatesPipeline' : 100,
    'athome.pipelines.becloud.AthomePipeline': 300,
#    'scrapy_mongodb.MongoDBPipeline': 900,
#    'athome.pipelines.scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 900,
#    'athome.pipelines.scrapy_firebase.FirebasePipeline': 900,
    'athome.pipelines.scrapy_arangodb.ArangodbPipeline': 900,
}

#MONGODB_URI = 'mongodb://mongodb.imply.lu:27017'
#MONGODB_DATABASE = 'scrapy'
#MONGODB_COLLECTION = 'athome-spider'
#MONGODB_UNIQUE_KEY = 'id'

#ELASTICSEARCH_SERVERS = ['https://elastic:kMOAxBOTmu54v4USuoE3XQqX@abf56f92bbfb005098d8af1ca642cd63.us-east-1.aws.found.io:9243']
#ELASTICSEARCH_INDEX = 'athome-property'
#ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m-%d'
#ELASTICSEARCH_TYPE = 'items'
#ELASTICSEARCH_UNIQ_KEY = 'id'  # Custom uniqe key

FIREBASE_SECRETS = """ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAi
cHJvcGVydHlzY3JhcGVyIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiZDk3NTRlZmMx
MGE2M2U3MThhNjA4OTFhNzE2MTQ2NzljNDQyOWMwNSIsCiAgInByaXZhdGVfa2V5
IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZnSUJBREFOQmdr
cWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFDdm9Ed090V01kVFJp
S1xuNDQvZW9Da3pndHdNaXVBRElDVjZsUnY2ZlVCVFZvWVdDeWwxTUhZMHBLVzE0
cUoyd2d0K0hYNVZ6NXR2UHF1cFxuZ0M4d2d4dWZkNU82VTFuVE93UkhjaHExUVpa
cFNzbmk2Q2V2S0g0UjV3T2ZqbmVQVmVCL1dOTG9jSzdwM0cwY1xuM0RjWmJZTW9W
S0hDajdzNjBqZ1I1UGhrNlpyeXEwbTYvL1dISVM2cVgvUm9ITmxFcHA4L2FzbGJo
ZlppeDVsdVxuUGk5Q0VscHZvUUpNWGtESTJyS2FjQ0dyRFZmcW5yWEU4ZDA3WVJN
YzdXNEl6ZVVMcSs5dVlwS0ZMUFdnTldZc1xueGF5UHhXVVZ3dUJYR0NRYTVxY2dq
bVZmM1BkTEo4ak52eW1kREVDOHRXdWltc0dxeE03eFlzbE1GMXhDb0NualxuVkJr
SFZQMVpBZ01CQUFFQ2dnRUFIOWcrMDQ3dHZod2kyVm82VmN4Mk5BNGtEczBtb2NK
ME1VWTB1TVo1d2JLMFxuWk81WXNkUmI5cDh0SWU0S2RkeW8vMURqUGJXRGNsZ3Jn
YlJKdWpMbnNSSmFVY1IzeXQ2T1g5TVBoekt4am4xK1xuWGx1b2lIRGY3U2lWaGxx
cmtLeXFaSVRyVnpUSmJvT21zRDg0Nlc0clJFYVdQeVJYTjJyek9rRnBqY2l5N1JH
MlxuMTM3T2pOY3A0R0NaTnpBbnp6WmxuSWNEa1ZCcHJpYUVrS3MvVW9Ea0FLSkps
REFoTGpZZ2ZXTFdXWmVUMHZHWlxueDREeVhzNTAwRkJEVGFnVE05c3RRbC9qVjJx
b1cyVXFNL29TczZHcjJYL1J1OVU3NlFDY21uZkF0K2NxMjIyYVxuRW5TdjhiZEZO
NnlyK3JrRkJQNHkyWDUyVEtzaFVyZ0lPQmRBbkgxMjlRS0JnUUR5cy9ITWpxSmJ0
dzViMGRXeFxuY3Q2ZmxFWUxqeVJMczNMQ3cvdHVNRGpGRzRQTkREcG5aN1V1ZEhL
Y1NWZy9yN3FReGwySXpEa3ZQaVhlME1YbFxuMWVWYzJPTld1QnduVGdsVUZiOFl6
ckN1anl6MlJBcS95VWtySENyRHFaa0pubjNxMVVJbkZiS0RUaVJOVWwwcVxucVhq
bVk2cnBkZUF0VllRNWlZTG1XL2dNSlFLQmdRQzVQMzZjOXlUMVdvZ01sdXFQQjNJ
VUdvZE51dm1wdVpDK1xucVloSFhrcFpnanN6c3pKQ1FQNFQyYWdiNTFRM3lOcjJZ
UEhuZkhUNU9BWmNKZEJkaHNlWlNjRVlzTFcwcmFvY1xuWDZiWGlONE1WL3dQZmIv
dk5qVHJEWlh5VW45RFIxT1ZEckFucWxrSkx2UDIvcFpuK0tCTkE4OVVDcnBidm4r
dFxudDBiQ08wdU1KUUtCZ1FDMUpZK2RBUHkzZmFyTzU1QWFzTVR1MElselNUUnEr
Qlg0dnJSa0tzUEVnbVBlWUhrYlxuQXZIZEtYYjlwVlNqdkRLQXFqM1h3NjRPejlF
T1BEN282N3dVajZFbThhVzV4R244QTNzdE5kL3plZE95UDFqU1xuaXBiOUFUbjk3
aERXZUNBOWJVekJ4VlVHNGdVQVhUQkNqbGs1aER4bG9lQmZsY3RwOG5Qc0ljckNy
UUtCZ1FDeVxua2xGejhBMnhjZ2FwMUNUaG9YVEhpbGNaaC82NUxJY3FNL1NKajR3
dVFvcmRLSVZ2Tm9WMkR4K3RYazVody8zR1xuK09iWGxiS1F0di95ZmdVZzB4YS9Y
a2lFaTN0dFl1Y1RtT1VVNmZ2YWZFb2ZpTUduVDJLdG54Z0hVcDBZOXIzTVxuZHk4
NTNVMGN2Q1V5MkhHV1lpWHNkNXE1VWVvWkhFYXA1MzJQS0dlSC9RS0JnSEp6Q3ds
d0RpTjJOUUNvb3gzUFxuZnZWSDI5UnpiT3FzbGc3YTJXbU45S01Bdzl6enNNUVNC
RzNCZGFXNzh6MENTY1Mrek0vc1NJeXZzVGhkbXAxWFxuRXNwREZUS0xZeHVrTEoy
UjhwZGo1WUJld0FVY1NBNy90SStwK3VQdnFzS3p2Mm5MMy9SYVM3OXljSzVlb1Fw
cFxuK0szUjk2ZzVTVEo1L2NRNS9mZ1VvSHFFXG4tLS0tLUVORCBQUklWQVRFIEtF
WS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAiZmlyZWJhc2UtYWRtaW5zZGst
aHZld2VAcHJvcGVydHlzY3JhcGVyLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwK
ICAiY2xpZW50X2lkIjogIjEwOTI5ODM5NzMxMjQ4NjA4OTgxNiIsCiAgImF1dGhf
dXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRo
IiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9v
L29hdXRoMi90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6
ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAog
ICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlz
LmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L2ZpcmViYXNlLWFkbWluc2RrLWh2
ZXdlJTQwcHJvcGVydHlzY3JhcGVyLmlhbS5nc2VydmljZWFjY291bnQuY29tIgp9
Cg==
"""
# Replace project-id to yours.
FIREBASE_DATABASE = 'https://propertyscraper.firebaseio.com/'
# Insert an appropriate value.
FIREBASE_REF = 'properties'
# To compose more robust child paths, you can add a list of properties.
FIREBASE_KEYS = ["id"]

ARANGODB_HOST = 'arango.imply.lu'
ARANGODB_USER = 'root'
ARANGODB_PWD = 'seatibiza'
ARANGODB_COL = 'properties'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
