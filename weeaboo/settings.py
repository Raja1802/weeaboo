BOT_NAME = 'weeaboo'

# Modules
NEWSPIDER_MODULE = 'weeaboo.spiders'
SPIDER_MODULES = ['weeaboo.spiders']
COMMANDS_MODULE = 'weeaboo.commands'

# Throttle
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 3

# Cache
HTTPCACHE_ENABLED = True
HTTPCACHE_GZIP = True
HTTPCACHE_EXPIRATION_SECS = 604800

# Pipelines
ITEM_PIPELINES = {
    'weeaboo.pipelines.storage.StoragePipeline': 0,
}

# Database
DATABASE_URL = 'file:weeaboo.db'

# Miscellaneous
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
