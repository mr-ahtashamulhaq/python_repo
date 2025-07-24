# Use requests.get() to fetch data from this URL:https://api.agify.io/?name=ahtasham
import requests
response = requests.get("https://api.agify.io/?name=ahtasham")
print(response.text)


# : Send Data Using POST
url = "https://httpbin.org/post"
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
data = {
    "name": "ahtasham",
    "email": "ahtasham@gmail.com"
}
response = requests.post(url, headers=headers, json=data)

print(response.text)