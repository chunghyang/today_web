
import requests
import urllib.request
import pandas as pd

query = input()
query = urllib.parse.quote(query)

client_id = "25MI09665QVPgSU5gZGo"
client_secret = "gPruKTcYci"

url = "https://openapi.naver.com/v1/search/shop.json?query="+query

request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)

response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

df = pd.DataFrame(response)


df[['title','lprice','mallName']]

