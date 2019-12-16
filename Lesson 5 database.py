import pymysql
# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='rutmwOjgbB', passwd='gzylgba5r3', db='rutmwOjgbB')




# import urllib.request
# val = urllib.request.urlopen("https://www.google.com").read()
# print(val)



import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])


import urllib.request, json
# Opening a web request
url = urllib.request.urlopen("http://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=dbebcc1e921dd03ab070")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)