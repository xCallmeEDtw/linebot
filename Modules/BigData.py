import requests as req
from bs4 import BeautifulSoup as mBS
import random
def RandomPicture(text):
    if text == '':
        web = 'https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500'
    else:
        web = f'https://wall.alphacoders.com/search.php?search={text}'

    r = req.get(web)
    myreply = []
    soup = mBS(r.text, 'html.parser')
    cards = (soup.select('[loading="lazy"]'))
    for i in range(0,len(cards),2):
        myreply.append(cards[i]['src'])
    MyRan =  random.randint(0,len(myreply)-1)
    #print(myreply,MyRan)
    return myreply[MyRan]


