# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field
from scrapy import Item


class TentopcrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LappyListItem(Item):
    """
    The items fields to be scraped for a Laptop
    """
    model = Field()
    budget = Field()
