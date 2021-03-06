import scrapy
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    #start_urls = ['http://127.0.0.1/maoyan.html']

    def parse(self, response):
        items = []
        #print ("++++++++++++++++++++++")
        #print (response.text)
        #print ("++++++++-----------------")
        films = Selector(response).xpath(
            '//div[@class="movie-item film-channel"]')
        for film_selector in films[:10]:
            item = {}
            # print(film_selector)
            s_title = film_selector.xpath(
                '../div[@class="channel-detail movie-item-title"]/@title')
            #print ("title is %s" % s_title.extract_first())
            s_type = film_selector.xpath(
                './div/a/div/div[2]/text()')
            
            s_date = film_selector.xpath(
                './div/a/div/div[4]/text()')
            #print (s_date)

            item['title'] = s_title.extract_first()
            item["film_type"] = s_type.extract()[1].strip()
            item['date'] = s_date.extract()[1].strip()
            items.append(item)
            
            print ("==================")
            
        return items
