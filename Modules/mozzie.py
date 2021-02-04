#myin = str(input())

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from bs4 import BeautifulSoup as mBS
def r6(text):
	print("hi")
	op_id = '[data-index="2:17"]'
	find_name = text

	nums,titles = [],[] 
	options = Options()
	options.add_argument("--disable-notifications")
	 
	chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

	chrome.get('https://r6.tracker.network/')
	sleep(2)
	chrome.find_element_by_css_selector('[name= "name"]').send_keys(find_name)
	sleep(1)
	chrome.find_element_by_css_selector('[type="submit"]').click()
	sleep(2)
	soup = mBS(chrome.page_source, 'html.parser')

	wins = (soup.select('[data-stat="PVPMatchesWon"]')[0].text).translate({ord("\n" ): None})
	print('Wins:',wins)
	winpers = (soup.select('[data-stat="PVPWLRatio"]')[0].text).translate({ord("\n" ): None})
	print('Win%:',winpers)
	sleep(1)
	chrome.find_element_by_css_selector('a[href*="operators"]').click()
	sleep(2)
	soup = mBS(chrome.page_source, 'html.parser')

	find_op = soup.select(op_id)[0].text.split()

	print('played time:',find_op[1],find_op[2])
	print('kills:',find_op[3])
	print('KD:',find_op[4])
	print('WINS:',find_op[5])
	print('Lossers:',find_op[6])
	print('你媽勝負比:',find_op[7])
	return(find_op)
#for a_kali in range()
