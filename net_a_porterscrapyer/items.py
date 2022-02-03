# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags 


# def remove_currency(value):
#     return value.replace('$','').strip()

# def remove_comma(value):
# 	 return value.replace(',','').strip()

class NetAPorterscrapyerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    brand = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    original_price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    sale_price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    image_url = scrapy.Field(output_processor = TakeFirst())
    product_page_url = scrapy.Field(output_processor = TakeFirst())
    product_category = scrapy.Field()
    


