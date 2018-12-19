import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1"

payload = ""
headers = {
    'applicationId': 
"E3D843F577E003A08553142B47616AE839D723B881731536F51F98D186CAD332",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
