import requests
import json
import sqllite3

conn = sqlite3.connect("test.db")
curr = conn.cursor()


print ('Scraping Data')

endpoints = ['Symbol', 'Name', ' Exchange']
base_url = "http://dev.markitondemand.com/Api/v2/"
lookup_url = base_url + "Lookup/"
quote_url = base_url + "Quote/"


print (lookup_url)
resp = requests.get(lookup_url + "json?input=NFLX")
# print (resp.headers)
# print (resp.encoding)
print (resp.text)
print (resp.json())

resp_json = resp.json()





resp = requests.get(quote_url + "json?symbol=NFLX")
print (resp.headers[high])
# print (resp.encoding)
print (resp.text)
