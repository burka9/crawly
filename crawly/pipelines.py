# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_url = os.getenv('MONGO_URL')
username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')


class DatabasePipeline:
    def __init__(self):
        try:
            self.client = MongoClient(mongo_url, username=username, password=password)
            self.db = self.client['crawly']
            self.collections = {}
        except Exception as e:
            print(e)
            raise DropItem('Failed to connect to the database')
    
    def process_item(self, item, spider):
        if spider.name == 'base_spider':
            raise DropItem('BaseSpider is not allowed to be used directly')
        else:
            return self.process_base_item(item, spider.name)
        
    def process_base_item(self, item, name):
        try:
            self.collections[name] = self.db[name]
            self.collections[name].create_index("url", unique=True)
        except Exception as e:
            pass

        try:
            self.collections[name].insert_one({
                'url': item['url'],
                'scrap_time': item['scrap_time'],
                'text': "" if 'text' not in item else item['text']
            })
        except Exception as e:
            raise DropItem('Failed to process item')