import requests

url = 
"https://kms1.kaiza.la/v1/bot/accessToken/f9d3a907-eef6-4bd7-9d98-9158a0cb05e4"

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
