# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class OtomotoItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()
    features = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()