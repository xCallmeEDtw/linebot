import requests as req
from bs4 import BeautifulSoup as mBS
import random
def RandomPicture(text):
    print("1")
    if text == '':
        web = 'https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500'
    else:
        web = f'https://wall.alphacoders.com/search.php?search={text}'
    headers= {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        #'cookie': '__cfduid=dde838dc1783d613c0da665ac3bd2f7571612245238; ckBahamutCsrfToken=aa43806cb40049fe; _ga=GA1.3.2147481981.1612245104; _gid=GA1.3.25827347.1612245104; ckBAHAADS={"FA":{"a0":2}}; ckBahaAd=-------------B--; __gads=ID=efb7856b96bbf722:T=1612245253:S=ALNI_MZIiDgRW0sEz5aVyAxERWHIzcOy3A; ckFORUM_bsn=23805; ckBH_lastBoard=[["23805","神魔之塔"]]; buap_modr=p020; buap_puoo=p402 p401; hahatoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJmaXJlYmFzZS1hZG1pbnNkay0ydGw0YkBoYWhhbXV0LTg4ODguaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJmaXJlYmFzZS1hZG1pbnNkay0ydGw0YkBoYWhhbXV0LTg4ODguaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJhdWQiOiJodHRwczpcL1wvaWRlbnRpdHl0b29sa2l0Lmdvb2dsZWFwaXMuY29tXC9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlhdCI6MTYxMjI0NTUxMiwiZXhwIjoxNjEyMjQ5MTEyLCJ1aWQiOiJndWVzdCIsImNsYWltcyI6eyJkZW55cG9zdCI6dHJ1ZSwibW9iaWxlIjpmYWxzZX19.F4GYZk-ANLOSYovqnUwdF3DkSPpZNH_YnJeB68Wy8aACO7Dre_oB40dH7jZHPrnTzeDmjxQOzxSAQJ2zrwEbu9vE35fNt0n0bNh8RSBSLUkX-mL2P_wsFFWQWyO1Xgu44ZPqoLt_4Clawo1rzXn6CnJBalImxIvQKLd06faxANyAQHr99VQv20lwz0Reg7g6uF7dDzgPix8NQ6jLElXbAzhI5JiynI0gws430z6IG276_gHsSqTSx1mYfReySTnO9GlCKzURZoCuiM2861n6AN6Sd7ibuRhz9-5-9cKUCQzwsRzLAS3jdJGNYHXi_2LZ32_TH_6uq2aebXVNB93ZXw'
    }
    print("2")
    r = req.get(web,headers=headers)
    print("3")
    myreply = []
    soup = mBS(r.text, 'html.parser')
    cards = (soup.select('[loading="lazy"]'))
    print("4")
    for i in range(0,len(cards),2):
        print(cards[i]['src'])
        myreply.append(cards[i]['src'])
    MyRan =  random.randint(0,len(myreply))
    return myreply[MyRan]


