
import requests
from bs4 import BeautifulSoup as bs
import re


class proizvod:
    def __init__(self, ime, cijena, link,oib):
        self.ime = ime
        self.cijena = cijena
        #self.opis = opis
        self.link = link
        self.oib=oib
    def ispis():
        return 0

def izvadilink(item):
    pad1 = re.compile('h3 class="entity-title"><a class="link" href="(.*?)" name')
    templink=str(pad1.findall(str(item)))
    templink=templink[2:-2]
    link='http://www.njuskalo.hr'+str(templink)
    return link

def izvadiime(item):
    pad1 = re.compile('<img alt="(.*?)" class="img entity-thumbnail-img"')
    temp=str(pad1.findall(str(item)))
    temp=temp[2:-2]
    ime=str(temp)
    return ime

"""
def izvadiopis(item):
    pad1 = re.compile('"entity-description-main(.*?)<br/>')
    temp=str(pad1.findall(str(item)))
    temp=temp[2:-2]
    opis=str(temp)
    return opis
"""

def izvadicijenu(item):
    pad1 = re.compile('<strong class="price price--hrk">(.*?) <span class="currency">')
    temp1=str(pad1.findall(str(item)))
    temp1=temp1[2:-2]
    temp2=int(temp1.replace('.',''))
    return temp2

def izvadioib(item):
    pad1 = re.compile('"hasCompare":false,"id":(.*?)}')
    temp1=str(pad1.findall(str(item)))
    temp1=temp1[2:-2]
    temp2=int(temp1.replace('.',''))
    return temp2

def getOglasi(url,price):
    import requests
    from bs4 import BeautifulSoup as bs
    import re    
    oglasi=scrap(url)
    oglasifilter=[]
    for item in oglasi:
        if item.cijena<=price:
            if item.cijena>100:
                oglasifilter.append(item)
    return oglasifilter

def scrap(url):
    r=requests.get(url)
    soup=bs(r.content,"lxml")
    i=0
    oglasi=[]
    data=soup.find_all("li",{"class": "EntityList-item--Regular"})

    for item in data:
       i=i+1
       link=izvadilink(item)
       ime=izvadiime(item)
       #opis=izvadiopis(item)
       cijena=izvadicijenu(item)
       oib=izvadioib(item)

       temp=proizvod(ime,cijena,link,oib)
       oglasi.append(temp)



    oglasi=sorted(oglasi, key=lambda proizvod: proizvod.cijena)

    return oglasi





