import requests

url = "https://api.kaiza.la/v1/webhook"

querystring = 
{"objectId":"df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1","objectType":"Group"}

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, 
params=querystring)

print(response.text)
