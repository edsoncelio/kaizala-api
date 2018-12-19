import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1"

payload = ""
headers = {
    'applicationId': "",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
