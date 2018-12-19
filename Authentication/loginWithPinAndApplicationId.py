import requests

url = "https://api.kaiza.la/v1/loginWithPinAndApplicationId"

payload = 
"{\"mobileNumber\":\"+5585996058401\",\"applicationId\":\"37ba1e41-d55c-43bf-a2fa-d72c97aa080a\", 
\"applicationSecret\":\"W2N7H1RW3V\", \"pin\":6823}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
