import re
from difflib import SequenceMatcher
import math
from collections import Counter
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from scrapy.contrib.loader import ItemLoader
from eventcrawler.items import EventcrawlerItem 
from scrapy.http import Request

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
        loader = ItemLoader(item=EventcrawlerItem(), response=response)
        loader.add_value('link',response.url)
        loader.add_value('score',self.find_similarity_score(self.start_urls[0],response.url,'seqmatcher'))
        return loader.load_item()


    def find_similarity_score(self,start_url,response_url,func):
        if func=='seqmatcher':
            sum=0
            for i in range(len(start_url.split('/'))):
                seq=SequenceMatcher(a=re.split('/|\?|\&|\=',start_url)[i].lower(),b=re.split('/|\?|\&|\=',response_url)[i].lower())
                sum+=float(seq.ratio())
            return sum
        elif func=='cosine':
            vec1=Counter(re.split('/|\?|\&|\=',start_url))
            vec2=Counter(re.split('/|\?|\&|\=',response_url))
            return self.get_cosine(vec1,vec2)

            
    def get_cosine(self,vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
           return 0.0
        else:
           return float(numerator) / denominator
       
