import requests

url = "https://api.kaiza.la/v1/generatePin"

payload = "{\"mobileNumber\":\"+919910870005\", 
applicationId:\"37ba1e41-d55c-43bf-a2fa-d72c97aa080a\"}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
