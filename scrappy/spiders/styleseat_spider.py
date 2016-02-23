import scrapy
import pprint

from scrappy.spiders.scrappy_spider import ScrappySpider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class StyleseatSpider(ScrappySpider):
    name = "styleseat"
    allowed_domains = ["styleseat.com"]
    start_urls = [
        'http://www.styleseat.com/search?q=Barber&loc=20878',
        'https://www.styleseat.com/search?sort=&qv=&q=Hair+Cut&loc=Dc&date=&end_date=&time_range=&loreal_brand_serp=',
        # 'https://www.styleseat.com/search',
        # 'https://www.styleseat.com/search',
        # 'https://www.styleseat.com/search',
        ]

    form_data = [
        {   'q': 'Barber',
            'loc': 20878 },
        {   'q': 'Weaves &amp; Extensions',
            'loc': 20878 },
        {   'q': 'Hair Cut',
            'loc': 20878 },
        {   'q': 'Style',
            'loc': 20878 },
        {   'q': 'Braids',
            'loc': 20878 },
        ]

    def parse(self, response):
        url = response.url
        s = Selector(response)
        soupy = self.get_parser(response.body)

        self.d(soupy)
        data = {
            url: url,
            # profiles: self.get_attributes(items.select('a.avatarLink'), 'href'),
            # pictures: self.get_attributes(items.select('a.avatarLink > img'), 'src'),
            # firstName: self.get_text(items.select('h3.resultTitle > a > span')),
            # profession: self.get_text(items.select('span.resultTagLine')),
            # business: self.get_text(items.select('span.resultTagline > span.resultBusiness')),
            # address: self.get_text(items.select('p.stylistAddress'))
            }

        return data