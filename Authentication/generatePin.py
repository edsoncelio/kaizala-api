import requests

url = "https://api.kaiza.la/v1/generatePin"

payload = "{'mobileNumber':"",'applicationId':""}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
