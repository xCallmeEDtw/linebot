def FlexEdit():
	flexMessage ={
	  "type": "bubble",
	  "hero": {
	    "type": "image",
	    "url": "https://images8.alphacoders.com/533/thumb-1920-533007.png",
	    "size": "full",
	    "aspectRatio": "20:13",
	    "aspectMode": "cover",
	    "action": {
	      "type": "uri",
	      "label": "Line",
	      "uri": "https://linecorp.com/"
	    }
	  },
	  "body": {
	    "type": "box",
	    "layout": "vertical",
	    "contents": [
	      {
	        "type": "text",
	        "text": "C8763",
	        "weight": "bold",
	        "size": "xl",
	        "contents": []
	      },
	      {
	        "type": "box",
	        "layout": "baseline",
	        "margin": "md",
	        "contents": [
	          {
	            "type": "icon",
	            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
	            "size": "sm"
	          },
	          {
	            "type": "icon",
	            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
	            "size": "sm"
	          },
	          {
	            "type": "icon",
	            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
	            "size": "sm"
	          },
	          {
	            "type": "icon",
	            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
	            "size": "sm"
	          },
	          {
	            "type": "icon",
	            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
	            "size": "sm"
	          },
	          {
	            "type": "text",
	            "text": "4.0",
	            "size": "sm",
	            "color": "#999999",
	            "flex": 0,
	            "margin": "md",
	            "contents": []
	          }
	        ]
	      },
	      {
	        "type": "box",
	        "layout": "vertical",
	        "spacing": "sm",
	        "margin": "lg",
	        "contents": [
	          {
	            "type": "box",
	            "layout": "baseline",
	            "spacing": "sm",
	            "contents": [
	              {
	                "type": "text",
	                "text": "Place",
	                "size": "sm",
	                "color": "#AAAAAA",
	                "flex": 1,
	                "contents": []
	              },
	              {
	                "type": "text",
	                "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
	                "size": "sm",
	                "color": "#666666",
	                "flex": 5,
	                "wrap": True,
	                "contents": []
	              }
	            ]
	          },
	          {
	            "type": "box",
	            "layout": "baseline",
	            "spacing": "sm",
	            "contents": [
	              {
	                "type": "text",
	                "text": "Time",
	                "size": "sm",
	                "color": "#AAAAAA",
	                "flex": 1,
	                "contents": []
	              },
	              {
	                "type": "text",
	                "text": "10:00 - 23:00",
	                "size": "sm",
	                "color": "#666666",
	                "flex": 5,
	                "wrap": True,
	                "contents": []
	              }
	            ]
	          }
	        ]
	      }
	    ]
	  },
	  "footer": {
	    "type": "box",
	    "layout": "vertical",
	    "flex": 0,
	    "spacing": "sm",
	    "contents": [
	      {
	        "type": "button",
	        "action": {
	          "type": "uri",
	          "label": "CALL",
	          "uri": "https://linecorp.com"
	        },
	        "height": "sm",
	        "style": "link"
	      },
	      {
	        "type": "button",
	        "action": {
	          "type": "uri",
	          "label": "WEBSITE",
	          "uri": "https://linecorp.com"
	        },
	        "height": "sm",
	        "style": "link"
	      },
	      {
	        "type": "spacer",
	        "size": "sm"
	      }
	    ]
	  }
	}
	return flexMessage