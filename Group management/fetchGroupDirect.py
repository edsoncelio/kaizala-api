import requests

url = "https://kms1.kaiza.la/v1/groups"

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
