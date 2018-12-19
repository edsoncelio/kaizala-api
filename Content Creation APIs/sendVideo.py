import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/actions"

payload = "{\n  actionType: \"Video\",\n  actionBody: {\n  
\tcaption:\"video Caption\",\n    
mediaResource:\"eyJBY3Rpb25UeXBlIjoxMCwiRmlsZXMiOlt7IklkIjoiNTQ5NTRhMDMtOTQ2OC00YjZjLTljY2MtNjE5ZDViMGRmNmVjIiwiTmFtZSI6IlNhbXBsZVZpZGVvXzEyODB4NzIwXzFtYi5tcDQiLCJTaXplIjoxMDU1LCJVcmwiOiJodHRwczovL2Nkbi5rYXNjb3JlLm9zaS5vZmZpY2UubmV0LzZhNDAzM2IyZTZmMmUzYzM2OWMzYjhkMDRjYmNiMDlhMjU4NjJjMDZlMzg3ZmI3MmMxOTU0OGJiYmQ0MjMwNzIubXA0P3N2PTIwMTUtMTItMTEmc3I9YiZzaWc9M1Vya2VZSlUxQ0tPR0QwNTQzU1RwOGR2VG5kQTRCMnI0JTJCYkt2MFFwZ2QwJTNEJnN0PTIwMTctMDktMTRUMTQlM0EzNyUzQTE2WiZzZT0yMjkxLTA2LTMwVDE1JTNBMzclM0ExNlomc3A9ciIsIkhlaWdodCI6NjQwLCJXaWR0aCI6NjQwfV19\"\n  
}\n}"
headers = {
    'Content-Type': "application/json",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
