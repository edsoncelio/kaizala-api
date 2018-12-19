import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/actions"

payload = "{\n  actionType: \"Document\",\n  actionBody: {\n  
\tcaption:\"document Caption\",\n    
mediaResource:\"eyJBY3Rpb25UeXBlIjo2LCJGaWxlcyI6W3siSWQiOiJmZjA3MjJhNy02NDMwLTRkN2QtYWE1Ny04MDQ5MjQ4ZGM1NTEiLCJOYW1lIjoiQm9vazEueGxzeCIsIlNpemUiOjEwLCJVcmwiOiJodHRwczovL2Nkbi5rYXNjb3JlLm9zaS5vZmZpY2UubmV0L2ZlMDExMTE2MTcyYWFiZjViNzhhNWY5YTAwOWU3NGM4ZWI1M2JhMzk0YmJjNDg2MTBjYTY3ODhkNmM2OGU3MzcueGxzeD9zdj0yMDE1LTEyLTExJnNyPWImc2lnPUVnRVZDdkxQUDFPMXF6dE5LbnE4d251bjM4aFBYdk8xYW4wNVBlQnpIaEUlM0Qmc3Q9MjAxNy0wNS0xN1QwOSUzQTM0JTNBNDdaJnNlPTIyOTEtMDMtMDJUMTAlM0EzNCUzQTQ3WiZzcD1yIn1dfQ==\"\n  
}\n}"
headers = {
    'Content-Type': "application/json",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
