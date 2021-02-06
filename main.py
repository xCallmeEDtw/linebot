# pip3 install -r requirements.txt 
from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
from Modules.OPTmessage import MessageAdd
from Modules.games import mora
from Modules.mozzie2 import r6_operater
from Modules.mozzie2 import r6_states
#from Modules.BigData import RandomPicture
from Modules.FlexEdit import FlexEdit
from Modules.MyScheduler import MyScheduler
import os
from bs4 import BeautifulSoup as Soup
import requests
MyScheduler()
# import random
app = Flask(__name__) #初始化
#HTTP請求方式
@app.route('/', methods=['GET', 'POST']) #根目錄
# {'type': 'message', 'replyToken': '401f1beb096e4bd094fca05f1162e588', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612339264295, 'mode': 'active', 'message': {'type': 'sticker', 'id': '13493434162018', 'stickerId': '140', 'packageId': '2', 'stickerResourceType': 'STATIC', 'keywords': ['chase', 'play', 'skip', 'enjoy', 'Happy']}}

def index():
	con = ['剪刀' ,'石頭','布']
	horos = ["水瓶",'雙魚','牡羊','金牛','雙子','巨蟹','獅子','處女','天平','天蠍','射手','魔羯']
	messages = []
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(request.get_json())
		#print(type(message))
		replyToken = message.get('replyToken')
		text = message.get('message').get('text')
		SplitText = text.split()
		print(text)
		print(SplitText)

		if text == 'ssd':
			messages.append(MessageAdd('go buy ssd la', 'text'))
			messages.append(MessageAdd([1,1], 'sticker'))
			messages.append(MessageAdd('https://images5.alphacoders.com/314/thumb-1920-314574.png', 'image'))
			ReplyMessage(replyToken,messages)
		elif text in con:
			myreply = mora(text)
			messages.append(MessageAdd(myreply[0], 'text'))
			messages.append(MessageAdd(myreply[1], 'text'))
			ReplyMessage(replyToken,messages)
		elif text in horos:
			myreply = find_horo(text)
			messages.append(MessageAdd(myreply, 'text'))
			ReplyMessage(replyToken,messages)

		elif SplitText[0] == 'r6' and len(SplitText) >= 3:
			if SplitText[1] == 'stats':
				myreply = r6_states(SplitText[2])
				messages.append(MessageAdd("Wins: " + myreply[0], 'text'))
				messages.append(MessageAdd("Win%: " + myreply[1], 'text'))
				ReplyMessage(replyToken,messages)
			elif SplitText[1] == 'operater' and len(SplitText) == 4:
				myreply = r6_operater(SplitText[2],SplitText[3])
				messages.append(MessageAdd('played time:' + myreply[1] +' '+myreply[2], 'text' ))
				messages.append(MessageAdd('kills:' + myreply[3] + ' KD:'+ myreply[4], 'text'))
				messages.append(MessageAdd('WINS:' + myreply[5] + ' Lossers:' + myreply[6], 'text'))
				messages.append(MessageAdd('Wins%:'+ myreply[7], 'text'))
				messages.append(MessageAdd('幹員特殊道具成功使用'+ myreply[-1] , 'text'))
				ReplyMessage(replyToken,messages)
		elif SplitText[0] == '抽':
			if len(SplitText) >= 2:
				myreply = RandomPicture(SplitText[1])
			else:
				myreply = RandomPicture('')
			messages.append(MessageAdd(myreply, 'image'))
			ReplyMessage(replyToken,messages)
		elif text == 'test':
			
			messages.append(MessageAdd(["caffee",FlexEdit(2)],'flex'))

			ReplyMessage(replyToken,messages)
		elif text == 'test2':
			proxyDict = {
		    "http"  : os.environ.get('FIXIE_URL', ''),
		    "https" : os.environ.get('FIXIE_URL', '')
			}

			url = "https://telebears.berkeley.edu/enrollment-osoc/osc"
			code = "26187"
			values = dict(_InField1 = "RESTRIC", _InField2 = code, _InField3 = "13D2")
			html = requests.post(url, params=values, proxies=proxyDict)
			soup = Soup(html.content, from_encoding="utf-8")

			sp = soup.find_all("div", {"class" : "layout-div"})[2]
			print(sp.text)




		return 'go buy ssd la mother fker'
	elif request.method == 'GET':
		return 'go buy ssd la mother fker'
	else:
		return 'go buy ssd la mother fker'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

