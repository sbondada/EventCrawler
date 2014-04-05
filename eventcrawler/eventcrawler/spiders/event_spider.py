from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item

class eventSpider(CrawlSpider):
    name="event"
    rules = (
            Rule(SgmlLinkExtractor(allow=('.*events.*',),unique=True),callback='parse_links'),
            ) 

    def __init__(self,start_url=None,*args,**kwargs):
        super(eventSpider,self).__init__(*args,**kwargs)
        self.start_urls=[start_url]
        self.allowed_domians=[start_url.split('/')[2]]
        
    
    def parse_links(self,response):
        self.log('Hi, this is an item page! %s' % response.url)

