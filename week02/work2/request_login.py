
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

USER_AGNET = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/8'

def shimo_login():
    login_url = 'https://shimo.im/lizard-api/auth/password/login'
    referer = 'https://shimo.im/login?from=home'
    form_data = {
        'email': '123@qqq.com',
        'mobile': '+86undefined',
        'password': '123456ctf',
    }
    headers = {
        'user-agent': USER_AGNET,
        'refere': referer,
    }
    s = requests.Session()
    r = s.post(login_url, data=form_data, headers=headers)

    print(dir(r))
    print (r.headers)
    print (s.cookies)
    
def eeworld_login():
    login_url = 'http://bbs.eeworld.com.cn/member.php'
    referer = 'http://bbs.eeworld.com.cn/member.php?mod=logging&action=phoneemail'
    headers = {
        'user-agent': USER_AGNET,
        'refere': referer,
    }
    s = requests.Session()
    r = s.post(login_url, data=form_data, headers=headers)

    print (r.headers)
    print (r.text)
    print (s.cookies)    
    
if __name__ == "__main__":
    shimo_login()
    
    print ("end")