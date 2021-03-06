# Scrapy settings for eventcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'eventcrawler'

SPIDER_MODULES = ['eventcrawler.spiders']
NEWSPIDER_MODULE = 'eventcrawler.spiders'
DEPTH_LIMIT = 5
DEPTH_PRIORITY = 0
DEPTH_STATS = True
ITEM_PIPELINES = {
                    'eventcrawler.pipelines.EventcrawlerPipeline': 300,
                 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eventcrawler (+http://www.yourdomain.com)'
