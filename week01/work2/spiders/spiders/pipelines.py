# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        data = [[item["title"], item["film_type"], item["date"]]]
        movie_info = pd.DataFrame(data=data)
        movie_info.to_csv("./maoyan_scrapy.csv", mode='a', encoding='utf-8',
                          index=False, header=False)
        return item
