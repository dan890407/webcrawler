import requests, json
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
rs=requests.session()
link=input("ppt link: ")
name=input("file name: ")
res = rs.get(link, headers=headers) 
soup=BeautifulSoup(res.text, 'html.parser')
href_list=[]
for entry in soup.find_all('div',class_='push'):
        href_list.append(entry.find('span',class_='f3 push-content').text)
with open(name+".txt",'a+',encoding="utf-8") as f:
    for com in href_list:
        count=0
        for i in com:
            if i != ":" and (i!=" " and count!=1):
                f.write(i)
            count+=1
        f.write("\n")
print(href_list)



    



