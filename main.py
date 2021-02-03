from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
from Modules.OPTmessage import MessageAdd
app = Flask(__name__)
#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
# {'type': 'message', 'replyToken': '401f1beb096e4bd094fca05f1162e588', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612339264295, 'mode': 'active', 'message': {'type': 'sticker', 'id': '13493434162018', 'stickerId': '140', 'packageId': '2', 'stickerResourceType': 'STATIC', 'keywords': ['chase', 'play', 'skip', 'enjoy', 'Happy']}}
def index():
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(message)
		print(type(message))
		replyToken = message.get('replyToken')
		text = message.get('message').get('text')
		print(text)
# {'type': 'message', 'replyToken': '4128834b76bc44159cbc7da6c3b6e36a', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612336487515, 'mode': 'active', 'message': {'type': 'text', 'id': '13493228092527', 'text': '有'}}
		# if message.
		if text == 'ssd':
			messages = []
			ReplyText(replyToken,"go buy ssd la!")
			ReplySticker(replyToken,'1','1')


		return 'SUCCEED'
	elif request.method == 'GET':
		return 'SUCCEED'
	else:
		return 'SUCCEED'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

