from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
app = Flask(__name__)
#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(message)
		replyToken = message.get('replyToken')

		messages = [
		    {
		        "type":"text",
		        "text":"Hello, world1"
		    }
		]

		ReplyMessage(replyToken,messages)

		return 'SUCCEED'
	elif request.method == 'GET':
		return 'SUCCEED'
	else:
		return 'SUCCEED'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

