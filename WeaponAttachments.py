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

Weapons = {}

# Data to be written
def WeaponsUpdate(WeaponNumber, Name,WeaponType, WeaponFeature, UnlockLevel, MaxLevel, Optics, Muzzle, Barrel, Underbarrel, Body, Stock, Magazine, Handle):
    Weapons[WeaponNumber] = {
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

    
# WeaponsUpdate(1, "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as")
# WeaponsUpdate(2, "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as", "as")
# print(Weapons)

for link in range(len(Weaponlinks)):
    try:
        #First get the name of weapon
        #Tables we need to fetch data from
        Tables = [4,5,6,7,8,9,10,11]
        url = Weaponlinks[link]
        page = requests.get(url)
        df_list = pd.read_html(page.text) # this parses all the tables in webpages to a list
        #Gets the weapon Name from table 2
        Table2 = df_list[2]
        WeaponName = Table2[1][0]
        #Gets the weapon type, weapon feature, unlock level, and maxlevel from table 1
        Table1 = df_list[1]
        WeaponType = Table1[1][0]
        WeaponFeature = Table1[1][1]
        UnlockLevel = Table1[1][2]
        MaxLevel = Table1[1][3]
        #pre-defind array since there are # 8 diffrent types of attatchmnets
        Attachments =[[],[],[],[],[],[],[],[]]

        for r in range(len(Tables)):
            Table = df_list[Tables[r]]
            for j in range(len(Table['Attachment'])):
                Attachments[r].append(Table['Attachment'][j])
            


        WeaponsUpdate(link, WeaponName, WeaponType, WeaponFeature, UnlockLevel, MaxLevel, Attachments[0], Attachments[1], Attachments[3] , Attachments[3], 
        Attachments[4], Attachments[5], Attachments[6], Attachments[7])

        print(Weapons)
    except(KeyError):
        print()

with open('result.json', 'w') as fp:
    json.dump(Weapons, fp)