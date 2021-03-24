import requests 

from bs4 import BeautifulSoup

#This scrapper gets all the links for each diffrent wepon type.

WeaponClasslinks = ['https://gamewith.net/cod-coldwar/article/show/21943#NEW', 'https://gamewith.net/cod-coldwar/article/show/21943#AR', 'https://gamewith.net/cod-coldwar/article/show/21943#SMG', 
'https://gamewith.net/cod-coldwar/article/show/21943#TR', 'https://gamewith.net/cod-coldwar/article/show/21943#LMG', 'https://gamewith.net/cod-coldwar/article/show/21943#SR', 'https://gamewith.net/cod-coldwar/article/show/21943#SR', 'https://gamewith.net/cod-coldwar/article/show/21943#HG', 
'https://gamewith.net/cod-coldwar/article/show/21943#SG', 'https://gamewith.net/cod-coldwar/article/show/21943#LN', 'https://gamewith.net/cod-coldwar/article/show/21943#ML']

for r in range(len(WeaponClasslinks)):
    page = requests.get(WeaponClasslinks[r])

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class='codcw_weapons')
    print(results)
    #The urls for diffrent cold war guns
    WeaponUrls=[]

    #get the div id from the html file
    # for ultag in soup.find(class='codcw_weapons'):
    #     #find the a's within
    #     for litag in ultag.find_all('a'):
    #         #get the href
    #         if litag.has_attr('href'):
    #             CWurls.append(ColdWarurl+litag.attrs['href'])

    # print(CWurls)