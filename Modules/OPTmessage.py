import json
def MessageAdd(m_add,m_type,messages):
    if m_type == 'sticker':
        messages.append( 
            {
                "type":"sticker",
                "packageId": m_add[0],
                "stickerId": m_add[1]
                
            }
        )
    elif m_type =='text':
        messages.append(
            {
                "type":"text",
                "text": m_add
            }
        )
    return messages
# {'type': 'message', 'replyToken': '401f1beb096e4bd094fca05f1162e588', 'source': {'userId': 'Udde25b6bc63d084bbbf55c53ff0826d4', 'type': 'user'}, 'timestamp': 1612339264295, 'mode': 'active', 'message': {'type': 'sticker', 'id': '13493434162018', 'stickerId': '140', 'packageId': '2', 'stickerResourceType': 'STATIC', 'keywords': ['chase', 'play', 'skip', 'enjoy', 'Happy']}}
