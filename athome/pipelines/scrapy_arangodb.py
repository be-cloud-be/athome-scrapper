# -*- coding: utf-8 -*-
from os import environ, path, getcwd
from base64 import b64decode

from athome.items import PropertyAnnouce
from scrapy.exporters import BaseItemExporter

import requests
import json

from arangodb.api import Client, Database, Collection

import logging

_logger = logging.getLogger(__name__)

class ArangodbPipeline(BaseItemExporter):

    def load_spider(self, spider):
        self.crawler = spider.crawler
        self.settings = spider.settings

    def open_spider(self, spider):
        self.load_spider(spider)

    def process_item(self, item, spider):
        if isinstance(item, PropertyAnnouce):
            doc = dict(self._get_serialized_fields(item))
            doc['_key'] = doc['id']
            
            url = "http://%s:8529/_db/propertyscraper/_api/import?collection=%s&type=list&onDuplicate=replace" % (self.settings['ARANGODB_HOST'],self.settings['ARANGODB_COL'])
            data = [ doc ]
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            auth = (self.settings['ARANGODB_USER'], self.settings['ARANGODB_PWD'])
            resp = requests.post(url, data=json.dumps(data), headers=headers, auth=auth)
            
            if 400 <= resp.status_code <= 499:
                _logger.info("Client Error %s: %s" % (resp.status_code, resp.text))
            elif 500 <= resp.status_code <= 599:
                _logger.info("Server Error %s: %s" % (resp.status_code, resp.text))
            else:
                _logger.info("Item %s stored as announce into arangodb" % (doc['_key']))
        else :
            doc = dict(self._get_serialized_fields(item))
            doc['_key'] = doc['id']
            
            url = "http://%s:8529/_db/propertyscraper/_api/import?collection=%s&type=list&onDuplicate=replace" % (self.settings['ARANGODB_HOST'],spider.firebase_raw_collection)
            data = [ doc ]
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            auth = (self.settings['ARANGODB_USER'], self.settings['ARANGODB_PWD'])
            resp = requests.post(url, data=json.dumps(data), headers=headers, auth=auth)
    
            if 400 <= resp.status_code <= 499:
                _logger.info("Client Error %s: %s" % (resp.status_code, resp.text))
            elif 500 <= resp.status_code <= 599:
                _logger.info("Server Error %s: %s" % (resp.status_code, resp.text))
            else:
                _logger.info("Item %s stored as announce into arangodb" % (doc['_key']))

        return item

    def close_spider(self, spider):
        pass
