import requests

url = "https://localhost/v1/tenant/findGroupsByQuery"

querystring = {"query":"wit","resultsOffset":"0","pageSize":"10"}

payload = ""
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, 
params=querystring)

print(response.text)
