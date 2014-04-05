from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item

class eventSpider(CrawlSpider):
    name="event"

    def __init__(self,start_url=None,*args,**kwargs):
        self.regex=self.construct_regex(start_url)
        self.rules = [ Rule(SgmlLinkExtractor(allow=(self.regex,),unique=True),callback='parse_links') ] 
        super(eventSpider,self).__init__(*args,**kwargs)
        self.start_urls=[start_url,"http://"+start_url.split('/')[2]]
        #self.start_urls=[start_url]
        self.allowed_domians=[start_url.split('/')[2]]

    def construct_regex(self,start_url):
        urlsplit=start_url.split('/')
        regex='http://'+urlsplit[2]
        for part in urlsplit[3:]:
            if part.isdigit():
                regex=regex+'/[0-9]+'
            elif part=='':
                regex=regex
            else:
                regex=regex+'/[0-9a-zA-z-=?&_]+'
        print "regular expression %s " % regex
        return  regex 
   
    
    def parse_links(self,response):
        self.log('Hi, this is an item page! %s' % response.url)

