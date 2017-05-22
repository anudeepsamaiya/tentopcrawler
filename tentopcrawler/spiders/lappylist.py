"""
This module contains spiders for lappylist.com
"""
import scrapy

class LappylistSpider(scrapy.Spider):
    """
    The Spider for lappylist.com
    """
    name = 'lappylist'
    allowed_domains = ['lappylist.com']
    start_urls = ['http://lappylist.com/']
    download_delay = 5.0

    def parse(self, response):
        # follow links to laptop category pages
        for href in response.xpath('//a[contains(@href, "laptop")]/@href'):
            yield response.follow(href, callback=self.parse_laptops)

    def parse_laptops(self, response):
        yield response.xpath('//title').extract_first()
