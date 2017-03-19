BOT_NAME = 'weeaboo'

# Modules
NEWSPIDER_MODULE = 'weeaboo.spiders'
SPIDER_MODULES = ['weeaboo.spiders']

# Throttle
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 5

# Cache
HTTPCACHE_ENABLED = True
HTTPCACHE_GZIP = True
HTTPCACHE_EXPIRATION_SECS = 604800

# Middlewares / Pipelines
DOWNLOADER_MIDDLEWARES = {
    'weeaboo.middlewares.beautifulsoup.BeautifulSoupMiddleware': 583,
    'weeaboo.middlewares.cleaner.CleanerMiddleware': 587,
}

ITEM_PIPELINES = {}

# Miscellaneous
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
TELNETCONSOLE_ENABLED = False
BEAUTIFULSOUP_PARSER = 'lxml'
