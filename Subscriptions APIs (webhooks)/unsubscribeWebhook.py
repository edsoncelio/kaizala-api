import requests

url = "https://api.kaiza.la/v1/webhook/"

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, data=payload, 
headers=headers)

print(response.text)
