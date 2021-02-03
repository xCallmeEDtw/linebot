import requests
import json

def ReplyMessage(replyToken,messages):
    #請使用自己的token
    accessToken = 'LTaTHoeYkfTYpyCtqRwQX2wlaQniteHxFQsrK6tRIGhtn+SLOA9Wef6oDEGtlBIrxFbQPNI3aNfdHLSgGELZRl2iCIwE1zYB2i0QA6K2CxoutgsNsHZr097uFTAfIA1Bdv/Dg83ud3qUpDa92w6FCQdB04t89/1O/w1cDnyilFU='

    headers ={
        'Content-Type':'application/json',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        "replyToken":replyToken,
        'messages':messages
    }
    url = 'https://api.line.me/v2/bot/message/reply'
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r
# def ReplyText(replyToken,text):
#     messages = [
#         {
#             "type":"text",
#             "text": text
#         }
#     ]
#     ReplyMessage(replyToken,messages)
#     return 0
# def ReplySticker(replyToken,st_id,pk_id):
#     messages = [
#         {
#             "type":"sticker",
#             "packageId": pk_id,
#             "stickerId": st_id
            
#         }
#     ]
#     ReplyMessage(replyToken,messages)
#     return 0
# {'type': 'message', 'replyToken': '401f1beb096e4bd094fca05f1162e588', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612339264295, 'mode': 'active', 'message': {'type': 'sticker', 'id': '13493434162018', 'stickerId': '140', 'packageId': '2', 'stickerResourceType': 'STATIC', 'keywords': ['chase', 'play', 'skip', 'enjoy', 'Happy']}}
