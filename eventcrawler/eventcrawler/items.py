from scrapy.item import Item, Field

class EventcrawlerItem(Item):
    link=Field()
    score=Field()
    pass
