import requests as req
from bs4 import BeautifulSoup as mBS
def find_horo(text):

	myDict = {
	 	"水瓶": '10',
	 	'雙魚': '11',
	 	'牡羊': '12',
	 	'金牛': '13',
	 	'雙子': '2',
	 	'巨蟹': '3',
	 	'獅子': '4',
	 	'處女': '5',
	 	'天平': '6',
	 	'天蠍': '7',
	 	'射手': '8',
	 	'魔羯': '9',
	 }
	web = f'https://astro.click108.com.tw/daily_10.php?iAstro={myDict.get(text)}'
	r = req.get(web)
	titles= []
	images = []
	#print(r.status_code)

	#print(r.text)
	soup = mBS(r.text, 'html.parser')
	TodayContent = soup.select('.TODAY_CONTENT')
	return(TodayContent[0].text)