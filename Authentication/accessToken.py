import requests

url = "https://api.kaiza.la/v1/accessToken"

payload = ""
headers = {
    'applicationId': "",
    'applicationSecret': "",
    'refreshToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
