# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import NotConfigured
import pymysql


class SpidersPipeline:
    def __init__(self, mysql_conf):
        self.mysql_conf = mysql_conf
        self.con = None
        self.cursor = None
        try:
            self.con = pymysql.connect(**mysql_conf)
            self.cursor = self.con.cursor()
        except Exception as e:
            print (e)
            print ("~~~~~~~~~~~~~~")

    @classmethod
    def from_crawler(cls, crawler):
        mysql_conf = crawler.settings.get('MYSQL_CONF')
        print (mysql_conf)
        if not mysql_conf:
            raise NotConfigured
        return cls(mysql_conf)
        
    def process_item(self, item, spider):
        #data = [[item["title"], item["film_type"], item["date"]]]
        if (self.cursor):
            print ("execute ------------")
            try:
                sqlstr = ('insert into movies (title, type, date) values'
                         '(\"%s\", \"%s\", \"%s\");'
                        % (item["title"], item["film_type"], item["date"]))
                self.cursor.execute(sqlstr)
                print (sqlstr)
                self.con.commit()
            except Exception as e:
                print ("======= mysql exception ======")
                print (e)
        return item

    def open_spider(self, spider):
        print ("+++++++ open_spider ++++++++")
        pass
    
    def close_spider(self, spider):
        print ("+++++++ close_spider ++++++++")
        pass

    def __exit__():
        if(self.cursor):
            self.cursor.close()

        if(self.con):
            self.con.close()

    
