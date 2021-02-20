from bs4 import BeautifulSoup as bs
import requests
#import pandas as pd


response=requests.get("https://www.flipkart.com/search?q=Phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")
obj=bs(response.content)
#	print(obj.prettify())
name=obj.findAll("div",{"class":"_4rR01T"})
price=obj.findAll("div",{"class":"_30jeq3 _1_WHN1"})
a=[]
fields=['Mobile','price']
print(len(name))
for i in range(0,len(name)):	
	a.append([name[i].text,price[i].text])

import csv
with open('data.csv','w') as x:
	y=csv.DictWriter(x,fieldnames=fields)
	y.writeheader()
	for i in a:
		y.writerow({'Mobile':i[0],'price':i[1]})

