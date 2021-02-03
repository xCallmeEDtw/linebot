from flask import Flask,request

app = Flask(__name__)

#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.get_json().get('events')[0]
		print(message)
		return 'buy ssd la'
	elif request.method == 'GET':
		return 'buy ssd b***ch'
	else:
		return 'tell u to buy ssd'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

