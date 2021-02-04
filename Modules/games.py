import random
def mora(text):
	con = ['剪刀' ,'石頭','布']
	result = ['You win~', "平手", '哈，輸了吧廢物']
	if text == con[0]:
		text =0
	elif text == con[1]:
		text = 1
	elif text == con[2]:
		text = 2
	myran = random.randint(0,2)
	if myran == text:
		myreply = result[1]
	elif (text == 0 and myran == 2) or (text == 1 and myran == 0) or (text == 2 and myran == 1):
		myreply = result[0]
	else:
		myreply = result[2]
	return [myran,myreply]
