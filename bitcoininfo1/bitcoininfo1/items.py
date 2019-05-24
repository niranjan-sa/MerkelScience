# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Bitcoininfo1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post = Field()
    page_number = Field()
    url = Field()
    author = Field()
    subject = Field()
    #time = Field()
    message_number = Field()