import requests

url = "https://api.kaiza.la/v1/bot/f9d3a907-eef6-4bd7-9d98-9158a0cb05e4"

payload = "{\r\n\t\"name\":\"Test Bot User from API after update\"\r\n}"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
