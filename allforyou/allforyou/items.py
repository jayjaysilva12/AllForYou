# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllforyouItem(scrapy.Item):
    urls = scrapy.Field()
    title = scrapy.Field()
    retailer_sku_code = scrapy.Field()
    desc = scrapy.Field()
    offer = scrapy.Field()
    out_of_stock = scrapy.Field()
    old_price = scrapy.Field()
    #model = scrapy.Field()
    #mpn = scrapy.Field()
    sku = scrapy.Field()
    #upc = scrapy.Field()
    #ean = scrapy.Field()
    #currency = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()
    #current_price = scrapy.Field()
    #primary_image_url = scrapy.Field()
    categories = scrapy.Field()
