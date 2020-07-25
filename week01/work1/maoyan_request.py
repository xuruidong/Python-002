
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def html_request(target_url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/8"

    h = {'user-agent': user_agent,
         'refere': 'https://maoyan.com/films',
         'cookie': 'uuid_n_v=v1; uuid=C5903BD0CE2411EAAE7D95D379FC6A674CAD97DA49154D50880331AFA67B49C3; _lxsdk_cuid=17383f5d5dcc8-0cccc999f06b82-1217444b-1fa400-17383f5d5dcc8; _lxsdk=C5903BD0CE2411EAAE7D95D379FC6A674CAD97DA49154D50880331AFA67B49C3; mojo-uuid=09abadbdcb25d22f3ef35016aa4bdf70; _csrf=802946ba246f1eee68e81a19e0aea0c037baace22d369e84f93bd3f32407d409; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595646794,1595655924; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595655934; __mta=45529755.1595646793830.1595655931208.1595655933906.6; _lxsdk_s=173850b1d30-89b-97a-f30%7C%7C1',
         }

    #target_url = "https://movie.douban.com/top250"
    
    response = requests.get(target_url, headers=h)

    print (response.text)
    print (response.status_code)
    return response.text

def get_film_info(text):
    result_items = []
    soup = bs(text, 'html.parser')
    movie_list = soup.find_all(
        'div', attrs={'class': 'movie-item film-channel'}, limit=10)
    #print (len(movie_list))
    for movie_item in movie_list:
        #hover = movie_item.find('div', attrs={'class': 'movie-hover-info'})
        #print (hover)
        hover_list = movie_item.find_all(
            'div', attrs={'class': 'movie-hover-title'}, recursive=True)
        #print ("***************")
        #print (hover_list)
        item = []
        for index, hover in enumerate(hover_list):
            if (index == 1):
                item.append(hover.get("title"))
                tmp = hover.text.strip().split("\n")
                item.append(tmp[1].strip())
            elif (index == 3):
                tmp = hover.text.strip().split("\n")
                item.append(tmp[1].strip())
            #print ("++++   ++++")
        result_items.append(item)
        #print ("=============")
    return result_items

def info_save(data):
    movie_info = pd.DataFrame(data=data)
    movie_info.to_csv("./movie.csv", encoding='utf-8',
                      index=False, header=False)



if __name__ == "__main__":
    url = "https://maoyan.com/films?showType=3"
    
    text = html_request(url)
    '''
    with open("maoyan.html", 'wb') as f:
        f.write(text.encode("utf-8"))
    
    with open("maoyan.html", "rb") as f:
        text = f.read().decode("utf-8")
        print (type(text))
    '''
    info = get_film_info(text)
    info_save(info)
    print ("end")