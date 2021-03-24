import pandas as pd
import requests
from bs4 import BeautifulSoup
import json


#This scrapper is the data from the Weapon Scrapper that gets all the weapon links from the home page
Weaponlinks = ['https://gamewith.net/cod-coldwar/article/show/21938', 'https://gamewith.net/cod-coldwar/article/show/22111', 'https://gamewith.net/cod-coldwar/article/show/21939', 
'https://gamewith.net/cod-coldwar/article/show/22397', 'https://gamewith.net/cod-coldwar/article/show/23226', 'https://gamewith.net/cod-coldwar/article/show/23090', 
'https://gamewith.net/cod-coldwar/article/show/21805', 'https://gamewith.net/cod-coldwar/article/show/22042', 'https://gamewith.net/cod-coldwar/article/show/22112', 
'https://gamewith.net/cod-coldwar/article/show/22113', 'https://gamewith.net/cod-coldwar/article/show/22398', 'https://gamewith.net/cod-coldwar/article/show/23225',
 'https://gamewith.net/cod-coldwar/article/show/23490', 'https://gamewith.net/cod-coldwar/article/show/21805', 'https://gamewith.net/cod-coldwar/article/show/22116', 
 'https://gamewith.net/cod-coldwar/article/show/22115', 'https://gamewith.net/cod-coldwar/article/show/23224', 'https://gamewith.net/cod-coldwar/article/show/23223', 
 'https://gamewith.net/cod-coldwar/article/show/22121', 'https://gamewith.net/cod-coldwar/article/show/22117', 'https://gamewith.net/cod-coldwar/article/show/23222', 
 'https://gamewith.net/cod-coldwar/article/show/22122', 'https://gamewith.net/cod-coldwar/article/show/22120', 'https://gamewith.net/cod-coldwar/article/show/23221', 
 'https://gamewith.net/cod-coldwar/article/show/22123', 'https://gamewith.net/cod-coldwar/article/show/22124', 'https://gamewith.net/cod-coldwar/article/show/22399', 
 'https://gamewith.net/cod-coldwar/article/show/22125', 'https://gamewith.net/cod-coldwar/article/show/22127', 'https://gamewith.net/cod-coldwar/article/show/23798', 
 'https://gamewith.net/cod-coldwar/article/show/22129', 'https://gamewith.net/cod-coldwar/article/show/22400', 'https://gamewith.net/cod-coldwar/article/show/23894', 
 'https://gamewith.net/cod-coldwar/article/show/23896', 'https://gamewith.net/cod-coldwar/article/show/23488']

WeaponsData = {}

# Data to be written
def WeaponsUpdate(Name,WeaponType, WeaponFeature, UnlockLevel, MaxLevel, Optics, Muzzle, Barrel, Underbarrel, Body, Stock, Magazine, Handle):
    Weapons ={
        Name : {
        "WeaponType" : WeaponType,
        "WeaponFeature" : WeaponFeature,
        "Unlock Level" : UnlockLevel,
        "Max Level" : MaxLevel,
        "Attatchments" : {
            "Optics": Optics,
            "Muzzle": Muzzle,
            "Barrel": Barrel,
            "Underbarrel": Underbarrel,
            "Body": Body,
            "Stock": Stock,
            "Magazine": Magazine,
            "Handle": Handle,
            
        },
        
    },

    }

    return Weapons

# for r in range(len(Weaponlinks)):
#     page = requests.get(WeaponClasslinks[r])

#     soup = BeautifulSoup(page.content, 'html.parser')
#     # results = soup.find('div', attrs={'class':'codcw_weapons'})
#     # table = results.find('table')
#     # table_body = table.find('tbody')
    
#     # print(table_body)
#     # #The urls for diffrent cold war guns
#     # WeaponUrls=[]
#     # break
#     url = WeaponClasslinks[r]
#     r = requests.get(url)
#     df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
#     df = df_list[1]
#     print(df)
#     df.head()
#     break


#     #get the div id from the html file
#     # for ultag in soup.find(class='codcw_weapons'):
#     #     #find the a's within
#     #     for litag in ultag.find_all('a'):
#     #         #get the href
#     #         if litag.has_attr('href'):
#     #             CWurls.append(ColdWarurl+litag.attrs['href'])

#     # print(CWurls)