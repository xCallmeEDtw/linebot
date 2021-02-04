import requests as req
from bs4 import BeautifulSoup as mBS
def getData(selecter,tags):
	return  mBS(str(selecter.select(tags)[0]),'html.parser').text.translate({ord("\n" ): None})
def r6_states(text):

	web = f'https://r6.tracker.network/profile/pc/{text}'

	r = req.get(web)

	soup = mBS(r.text, 'html.parser')

	wins = getData(soup,'[data-stat="PVPMatchesWon"]')
	winpers = getData(soup, '[data-stat="PVPWLRatio"]')
	return(wins,winpers)
def r6_operater(player,operator):
	op_id ={
	'kali': '[data-index="2:17"]'
	
	}
	web = f'https://r6.tracker.network/profile/pc/{player}/operators'

	r = req.get(web)

	soup = mBS(r.text, 'html.parser')

	myreply = soup.select(op_id.get(operator))[0].text.split()

	print('played time:',myreply[1],myreply[2])
	print('kills:',myreply[3])
	print('KD:',myreply[4])
	print('WINS:',myreply[5])
	print('Lossers:',myreply[6])
	print('你媽勝負比:',myreply[7])
	
	return(myreply)



