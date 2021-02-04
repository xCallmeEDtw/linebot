import requests as req
from bs4 import BeautifulSoup as mBS
def getData(selecter,tags):
	return  mBS(str(selecter.select(tags)[0]),'html.parser').text.translate({ord("\n" ): None})
def r6_states(text):

	web = f'https://r6.tracker.network/profile/pc/{text}'

	r = req.get(web)

	titles= []
	images = []

	soup = mBS(r.text, 'html.parser')

	wins = getData(soup,'[data-stat="PVPMatchesWon"]')
	winpers = getData(soup, '[data-stat="PVPWLRatio"]')
	return(wins,winpers)
	# print('Wins:',wins)
	# print('Win%:',winpers)