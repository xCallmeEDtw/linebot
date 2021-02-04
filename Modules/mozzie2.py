import requests as req
from bs4 import BeautifulSoup as mBS
def r6_player_states(text):
	web = 'https://r6.tracker.network/profile/pc/'
	#add_web = str(input("輸入要查的玩家 "))
	web += text
	r = req.get(web)

	titles= []
	images = []
	print(r.status_code)

	#print(r.text)
	soup = mBS(r.text, 'html.parser')
	wins = (soup.select('[data-stat="PVPMatchesWon"]')[0].text).translate({ord("\n" ): None})
	print('Wins:',wins)
	winpers = (soup.select('[data-stat="PVPWLRatio"]')[0].text).translate({ord("\n" ): None})
	print('Win%:',winpers)