import os
import requests
from bs4 import BeautifulSoup as mBS
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def RandomPicture(text):
    print('123')
    myreply = []
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless") #無頭模式
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    print('345')
    #chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
    chrome.get('https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500')
    sleep(3)
    soup = mBS(chrome.page_source, 'html.parser')
    #print(soup)
    cards = (soup.select('[loading="lazy"]'))
    
    #print(cards)
    for i in range(0,len(cards),2):
       # print(cards[i])
        myreply.append(cards[i]['src'])
    MyRan =  random.randint(0,len(myreply))
    #print(myreply,MyRan)
    return myreply[MyRan]



# def RandomPicture(text):
#     # if text == '':
#     web = 'https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500?key=cae38234-ad07-43e9-b14e-36ff23e0c56b'
#     # else:
#     #     web = f'https://wall.alphacoders.com/search.php?search={text}'
#     headers= {
#     ':authority' : 'wall.alphacoders.com',
#     ':method' :'GET',
#     ':path' :'/by_category.php?id=3&name=Anime+Wallpapers',
#     ':scheme' : 'https',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     'cookie':' __cfduid=dbdf4b83daaefb87b1659554dc7752c801612489226; wa_session=t9j0jgadt1fp5vsdrvngqn6v1hqpqjfsvkrcgklanermu6qtnhfk5up40cukaqjhni34rt9ogutin427nsgv7l4hh4hffki58lmcr51; _ga=GA1.2.71696367.1612489087; _gid=GA1.2.383992023.1612489087; __cf_bm=e159d5b7948ac18e79c7b945e010965cbfe82dae-1612489228-1800-AVm7EKZUh/iPzfEKPeSDNPRtPcCbvChfmLlNaAefLd10HKzxrj++d4F1y+y8iGn9nujUfytd7yWBkdAo84M1bEVzQG0iqvptRvTIwWl6bE2OFy03IFL+6ByxyYako1CMog==; _gd1612489089261=1; _pbjs_userid_consent_data=3524755945110770; _pubcid=9251f950-4e88-4efc-8ec3-90476b175851; cto_bidid=uBBoaV94QmFNUHZTTjFtTWd5MFhySUludTJ5dWJlb2xiRDZUZ254dmRHeDdhU1lROXhxVHcyTUl3bVB5aVhxN21vSHZjaDNUQWk4Zk94RVhSdHRkcExxcFdYQSUzRCUzRA; cto_bundle=LOMq0l9pakt6alV5aUQ4MkllNmh3S3ZYdEM4JTJCNGJCNU8lMkJZbkNlNjR5Yk92JTJCZHNYWThlUE9kRiUyRjYlMkJTWXNGamtVcmFZWkM5SDFhVGhvN29EdmZhNVVyVHBNY3dPVGl3JTJCOFkydjhqc2ROQSUyQlRTdTdiVm4zcnJKQ0lVU09DNXRSSnlBa1Ju; __gads=ID=1a9626c30699371a:T=1612489229:S=ALNI_Mb82i5rqXZOdQnViPvDERa7wAOffA',
#     'referer': 'https://www.google.com/',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',

#     }
#     r = requests.get(web,headers, auth=HerokuBearerAuth('cae38234-ad07-43e9-b14e-36ff23e0c56b'))
#     myHeaders = {'Accept': 'application/vnd.heroku+json; version=3'} 
#     #r = requests.get('https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500?key=cae38234-ad07-43e9-b14e-36ff23e0c56b', headers=headers, auth=HerokuBearerAuth('cae38234-ad07-43e9-b14e-36ff23e0c56b')) 
#     print(r.status_code)
#     myreply = []
#     soup = mBS(r.text, 'html.parser')
#     cards = (soup.select('[loading="lazy"]'))
#     for i in range(0,len(cards),2):
#         myreply.append(cards[i]['src'])
#     MyRan =  random.randint(0,len(myreply)-1)
#     #print(myreply,MyRan)
#     return myreply[MyRan]


