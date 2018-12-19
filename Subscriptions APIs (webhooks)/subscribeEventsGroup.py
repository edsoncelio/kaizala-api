import requests

url = "https://api.kaiza.la/v1/webhook"

payload = "{  \r\n   
\"objectId\":\"df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1\",\r\n   
\"objectType\":\"Group\",\r\n   \"eventTypes\":[\r\n      
\"ActionCreated\",\r\n      \"ActionResponse\",\r\n      
\"SurveyCreated\",\r\n      \"JobCreated\",\r\n      
\"SurveyResponse\",\r\n      \"JobResponse\",\r\n      
\"TextMessageCreated\",\r\n      \"AttachmentCreated\",\r\n      
\"Announcement\",\r\n      \"MemberAdded\",\r\n      
\"MemberRemoved\",\r\n      \"GroupAdded\",\r\n      
\"GroupRemoved\",\r\n      \"PollCreated\",\r\n      
\"LetsMeetCreated\",\r\n      \"PollResponse\",\r\n      
\"LetsMeetResponse\"\r\n   ],\r\n   
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
