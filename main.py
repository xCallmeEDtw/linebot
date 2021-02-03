from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
app = Flask(__name__)
#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def myreply(replyToken , text):
		messages = [
		    {
		        "type":"text",
		        "text": text
		    }
		]

		return ReplyMessage(replyToken,messages)


def index():
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(message)
		print(type(message))
		replyToken = message.get('replyToken')
		text = message.get('message').get('text')
# {'type': 'message', 'replyToken': '4128834b76bc44159cbc7da6c3b6e36a', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612336487515, 'mode': 'active', 'message': {'type': 'text', 'id': '13493228092527', 'text': '有'}}
		# if message.
		if text == 'ssd':
			myreply(replyToken, "go but ssd la!")


		return 'SUCCEED'
	elif request.method == 'GET':
		return 'SUCCEED'
	else:
		return 'SUCCEED'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

