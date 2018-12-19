import requests

url = "https://api.kaiza.la/v1/groups"

querystring = {"fetchAllGroups":"true","showDetails":"true"}

payload = ""
headers = {
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, 
params=querystring)

print(response.text)
