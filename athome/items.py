# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyAnnouce(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    id = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    
    lat = scrapy.Field()
    lng = scrapy.Field()
    
    year_built = scrapy.Field()
    ground_surface = scrapy.Field()
    price = scrapy.Field()
    
    inserted = scrapy.Field()
    modification_date = scrapy.Field()