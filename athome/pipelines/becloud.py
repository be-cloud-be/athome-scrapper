# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from athome.items import PropertyAnnouce
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()
        self.ids_seen_raw = set()

    def process_item(self, item, spider):
        if isinstance(item, PropertyAnnouce):
            if item['id'] in self.ids_seen:
                raise DropItem("Duplicate item found drop it : %s" % item['id'])
            else:
                self.ids_seen.add(item['id'])
                return item
        else:
            if item['id'] in self.ids_seen_raw:
                raise DropItem("Duplicate raw item found drop it : %s" % item['id'])
            else:
                self.ids_seen_raw.add(item['id'])
                return item

class AthomePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,dict):
            pictures_old = item['pictures']
            if pictures_old:
                pictures_new = []  
                for x in range(1, 10):
                    if pictures_old and pictures_old['picture%d' % x]:
                        pictures_new.append({
                            'index' : x,
                            'src' : "https://i1.static.athome.eu/images/annonces2/image_%s" % pictures_old['picture%d' % x],
                            'text' : pictures_old['textpic%d' % x],
                        })
                item['pictures'] = pictures_new
            
            return item
        else:
            return item
