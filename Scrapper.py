import requests 

from bs4 import BeautifulSoup

ColdWarurl = 'https://gamewith.net/cod-coldwar/article/show/21943'

page = requests.get(ColdWarurl)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='toc')

#The urls for diffrent cold war guns
CWurls=[]

#get the div id from the html file
for ultag in soup.find(id='toc'):
    #find the a's within
    for litag in ultag.find_all('a'):
        #get the href
        if litag.has_attr('href'):
            CWurls.append(ColdWarurl+litag.attrs['href'])

print(CWurls)