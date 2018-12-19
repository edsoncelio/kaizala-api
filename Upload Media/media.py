import requests

url = "https://api.kaiza.la/v1/media"

headers = {
    'accessToken': "",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
