# -*- coding: utf-8 -*-
import scrapy
import json

from athome.items import PropertyAnnouce

class AthomeVenteMaisonSpider(scrapy.Spider):
    name = 'athome_vente_maison'
    allowed_domains = ['athome.lu']
    start_urls = ['http://athome.lu/']
    
    firebase_raw_collection = 'athome-spider'

    def parse(self, response):
        # Extract data from property pages
        for property_json in response.xpath("//script[contains(., 'initGoogleMap')]/text()").re("initGoogleMap\((\[.*\]).*\)"):
            property = json.loads(property_json)
            # Add url and title
            property = property[0]
            property['title'] = response.xpath('//title/text()').extract()[0]
            property['url'] = response.request.url
            yield property
            properyItem = PropertyAnnouce(
                id = 'athome-%s' % property['id'],
                source = 'athome',
                title = property['title'],
                description = property['description'],
                url = property['url'],
                lat = property['lat'],
                lng = property['lng'],
                year_built = property['year_built'],
                ground_surface = property['ground_surface'],
                price = property['price'],
                inserted = property['inserted'],
                modification_date = property['modification_date'],
            )
            yield properyItem
            
        # Follow all link starting with /vente/maison
        for href in response.css('a::attr(href)').re('(\/vente\/maison/.*)$'):
            yield response.follow(href, callback=self.parse)