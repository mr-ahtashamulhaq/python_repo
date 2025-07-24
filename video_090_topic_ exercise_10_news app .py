# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application
import requests

myapi = "a34a86ef25cb4f20a6534f7ae915ff0c"
url = "https://newsapi.org/v2/top-headlines"


print("\t\t---- WELCOME TO NEWS ----")
print("Choose Topic for news :\n")
print("1. business\n2. entertainment\n3. general\n4. health\n5. science\n6. sports\n7. technology\n")



topic_user = int(input("\npress number which news you want : "))
topics = ["business","entertainment","general","health","science","sports","technology"]



params = {"category" : topics[topic_user - 1] , 
          "apiKey" : "a34a86ef25cb4f20a6534f7ae915ff0c"}


response  = requests.get(url, params=params)
data = response.json()
for i, article in enumerate(data["articles"]):
  
  print(f"\n\n{i+1}:\n\t{article['title']}\n")
