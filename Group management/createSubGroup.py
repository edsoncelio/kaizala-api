import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/subgroups"

payload = "{name:\"Kaizala Test sub group\", welcomeMessage:\"Welcome to 
sub group created programmatically via Postman\", 
members:[\"+911199999999\"], groupType:\"Group\"}"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
