# -*- coding: utf-8 -*-
import scrapy
import json
import dateparser

from athome.items import PropertyAnnouce

class ImmoTopVenteMaisonSpider(scrapy.Spider):
    name = 'immotop_vente_maison'
    allowed_domains = ['immotop.lu']
    start_urls = ['https://www.immotop.lu/properties/house/house/index1.html']
    
    firebase_raw_collection = 'immotop-spider'

    def parse(self, response):
        if response.xpath("//script[contains(., 'listing_id')]/text()") :
            
            id = "immotop-%s" % response.xpath("//script[contains(., 'listing_id')]/text()").re("listing_id = '(\d+)'")[0]
            
            properyItem = PropertyAnnouce(
                    id = "immotop-%s" % response.xpath("//script[contains(., 'listing_id')]/text()").re("listing_id = '(\d+)'")[0],
                    source = 'immotop',
                    title = response.xpath('//title/text()')[0].extract(),
                    description = response.xpath("//meta[@name='description']/@content")[0].extract(),
                    url = response.request.url,
                    lat = response.xpath("//script[contains(., 'xlat')]/text()").re("xlat = (\d+\.\d+)")[0],
                    lng = response.xpath("//script[contains(., 'xlon')]/text()").re("xlon = (\d+\.\d+)")[0],
                    year_built = "",
                    ground_surface = response.xpath("//span[starts-with(@data-tip,'Surface du terrain')]").re("\d+\,\d+")[0].replace(',','.') if response.xpath("//span[starts-with(@data-tip,'Surface du terrain')]") else 10,
                    price = response.xpath('//div[@class="price_final"]/text()').extract()[0][2:].replace(' ','') if response.xpath('//div[@class="price_final"]/text()') else 0,
                    inserted = "",
                    modification_date = dateparser.parse(response.xpath("//*[contains(., 'Mise ')]/span").re('\((.*)\)')[0]).strftime("%Y-%m-%d") if response.xpath("//*[contains(., 'Mise ')]/span") else ""
                )
            yield properyItem
        
        # Follow all link starting with /vente/maison
        for href in response.css('a::attr(href)').re('(\/house\/house/.*)$'):
            yield response.follow(href, callback=self.parse)
        for href in response.css('a::attr(href)').re('(\/properties\/used\/house/.*)$'):
            yield response.follow(href, callback=self.parse)