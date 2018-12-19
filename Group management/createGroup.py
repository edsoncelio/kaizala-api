import requests

url = "https://kms1.kaiza.la/v1/groups"

payload = "{name:\"Kaizala Test group\", welcomeMessage:\"Welcome to 
group created programmatically via Postman\",groupType:\"Group\", 
ShortDescriptionString:\"Short description\", 
LongDescriptionString:\"Long description\"}"
headers = {
    'accessToken':"",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
