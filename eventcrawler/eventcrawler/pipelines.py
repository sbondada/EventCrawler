# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class EventcrawlerPipeline(object):
    
    items=[]

    def __init__(self):
        self.file=open('outlinks.jl','wb')

    def process_item(self, item, spider):
        line=json.dumps(dict(item))+"\n"
        self.file.write(line)
        self.items.append((item['score'],item['link']))
        self.items=sorted(self.items,reverse=True)
        self.results=open('toplinks.jl','wb')
        for tup in self.items[:10]:
            self.results.write(tup[1][0]+'\n')
        return item
