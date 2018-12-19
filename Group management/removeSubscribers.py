import requests

url = "https://api.kaiza.la/v1/groups//subscribers/remove"

payload = "{subscribers:[\"+91109999999\"]}"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
