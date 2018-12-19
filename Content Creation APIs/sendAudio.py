import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/actions"

payload = "{\n  actionType: \"Audio\",\n  actionBody: {\n  
\tcaption:\"audio Caption\",\n    
mediaResource:\"eyJBY3Rpb25UeXBlIjo1LCJGaWxlcyI6W3siSWQiOiJjMTA0ODU5My02NDBiLTQ4YTItYmY2ZC1mZTJhNTZjMzJlYTIiLCJOYW1lIjoiMTVrei0wNjQubXAyIiwiU2l6ZSI6MTIwLCJVcmwiOiJodHRwczovL2Nkbi5rYXNjb3JlLm9zaS5vZmZpY2UubmV0L2JmM2NhMzM4MDE0ZWRkODAxNWRkOGY1N2QxNzZhYWZiODYxNTMwNTUzNWFhMzFhYTBiMWNiZTg5ZDA3NGUyZGUubXAyP3N2PTIwMTUtMTItMTEmc3I9YiZzaWc9THhkUW1mdUNHOURPclJxUFVBNEhQcnZaa2hZQUtwRThiUFI3UTBuTDd4OCUzRCZzdD0yMDE3LTA5LTE0VDE0JTNBNDElM0E1Nlomc2U9MjI5MS0wNi0zMFQxNSUzQTQxJTNBNTZaJnNwPXIiLCJIZWlnaHQiOjY0MCwiV2lkdGgiOjY0MH1dfQ==\"\n  
}\n}"
headers = {
    'Content-Type': "application/json",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
