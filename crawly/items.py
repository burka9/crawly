# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join, TakeFirst


class BaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    scrap_time = scrapy.Field(output_processor=TakeFirst())
    text = scrapy.Field(output_processor=TakeFirst())
