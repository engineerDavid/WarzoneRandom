import pandas as pd
import requests
from bs4 import BeautifulSoup

#3/23/2021
#This scrapper gets all the links for each diffrent weapon type.

#home link for wepons
Weaponslink = 'https://gamewith.net/cod-coldwar/article/show/21943#New'

page = requests.get(Weaponslink)

soup = BeautifulSoup(page.content, 'html.parser')

#list to keep track of all the links for the 35 diffrent weapons in warzone
WeaponUrls=[]


#get the div id from the html file
for ultag in soup.find_all('div', attrs={'class':'codcw_weapons'}):
    #find the a's within the class
    for litag in ultag.find_all('a'):
        #get the link from the <a>
        if litag.has_attr('href'):
            WeaponUrls.append(litag.attrs['href'])

    

 