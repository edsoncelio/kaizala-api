import requests

url = "https://api.kaiza.la/v1/webhook"

payload = "{  \r\n   \"objectId\":\"\",\r\n   
\"objectType\":\"Action\",\r\n   \"eventTypes\":[  \r\n      
\"ActionCreated\",\r\n      \"ActionResponse\"\r\n   ],\r\n   
\"callBackUrl\":\"https://requestb.in/12786un1\",\r\n   
\"callBackToken\":\"tokenToBeVerifiedByCallback\",\r\n   
\"callBackContext\":\"Any data which is required to be returned in 
callback. Current webhook data can be seen by refreshing: 
https://requestb.in/12786un1?inspect\"\r\n}"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
