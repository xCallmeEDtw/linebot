# pip3 install -r requirements.txt 
from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
from Modules.OPTmessage import MessageAdd
app = Flask(__name__) #初始化
#HTTP請求方式
@app.route('/', methods=['GET', 'POST']) #根目錄
# {'type': 'message', 'replyToken': '401f1beb096e4bd094fca05f1162e588', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612339264295, 'mode': 'active', 'message': {'type': 'sticker', 'id': '13493434162018', 'stickerId': '140', 'packageId': '2', 'stickerResourceType': 'STATIC', 'keywords': ['chase', 'play', 'skip', 'enjoy', 'Happy']}}
def index():
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(request.get_json())
		print(type(message))
		replyToken = message.get('replyToken')
		text = message.get('message').get('text')
		print(text)
		
		if text == 'ssd':
			messages = []
			messages.append(MessageAdd('go buy ssd la', 'text'))
			messages.append(MessageAdd([1,1], 'sticker'))
			messages.append(MessageAdd('https://images5.alphacoders.com/314/thumb-1920-314574.png', 'image'))
			ReplyMessage(replyToken,messages)

		return 'go buy ssd la mother fker'
	elif request.method == 'GET':
		return 'go buy ssd la mother fker'
	else:
		return 'go buy ssd la mother fker'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

