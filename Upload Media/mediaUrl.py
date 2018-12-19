import requests

url = "https://api.kaiza.la/v1/media/url"

payload = 
"{mediaUrl:\"https://manage.kaiza.la/Images/landing-images/main-page-1.png\"}"
headers = {
    'accessToken': "",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
