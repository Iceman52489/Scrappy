import os
import scrapy
import json
import requests
import copy
import re
import pprint

from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup

class ScrappySpider(scrapy.Spider):
    name = 'scrappy'
    pretty = pprint.PrettyPrinter(indent=4)
    start_urls = []
    form_data = []

    def __init__(self, *args, **kwargs):
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, 'config.json')

        with open(config_path) as config:
            config = json.load(config)

        super(ScrappySpider, self).__init__(*args, **kwargs)

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)

    # def make_requests_from_url(self, url):
    #     return Request(
    #         url,
    #         method = True,

    #         dont_filter = True
    #         )
    #def start_requests(self):
        #urls, params = self.start_urls, self.form_data
        #self.d(self)
        # for int_url, url in enumerate(urls):
        #     self.d(int_url)
            #
            # return scrapy.FormRequest(
            #     url,
            #     formdata = param,
            #     callback = self.parse
            # )

    def d(self, *var):
        self.pretty.pprint(var)

    def get_parser(self, html):
        html = re.sub("\n", " ", html)
        soupy = BeautifulSoup(html, 'html.parser')
        return soupy

    def get_attributes(items=[], attribute=None):
        d(items)
        #for intItem, item in items:

        #     if attribute is not None:
        #         self.d(item)
        #        #items[intItem] = item.get(attribute)

        return items

    def get_texts(self, *items):
        for intItem, item in items:
            items[intItem] = item.get_text()

        return items