import requests

url = 
"https://kms1.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/messages"

payload = "{message:\"Test message via API\"}\r\n"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
