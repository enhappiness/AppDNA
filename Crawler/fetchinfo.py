# -*- coding: UTF-8 -*-
import collections
from Crawler import TCrawler
import sys
sys.path.append("../Analyse")
from extract_keyword import KeyWordExtract

#import urllib2
##import jieba
#from bs4 import BeautifulSoup
#import collections
#
#
#class TCrawler:
#    def __init__(self):
#        pass
#    @staticmethod
#    def getText(url):
#        return urllib2.urlopen(url).read()
#
#    @staticmethod
#    def getSoup(text,lib="html5lib"):
#        return BeautifulSoup(text,lib)
#
#    def filter():
#        pass

baseUrl ="http://apps.wandoujia.com/"  
f = open("data.txt","w")
dic = collections.defaultdict(lambda:"")
temp = TCrawler.getText(baseUrl) 
soup = TCrawler.getSoup(temp)
#soup = BeautifulSoup(temp.read(),"html5lib")
#text = soup.find("div",class_="description").get_text()
arr = soup.find_all("a",class_ = "icon-area")
links = [ baseUrl + item["href"] for item in arr ]
detail = [ TCrawler.getText( item ) for item in links ]
soups =   [ TCrawler.getSoup(item) for item in detail]
for item in soups:
    name = item.find("h2",id="app-title").text 
    dic[name] += item.find("div",id="desc").text
    #f.write(name.encode("utf8")+" --> " + dic[name].encode("utf8")  + "\n") 
    #f.write(name.encode("utf8") + ":" +
    #        KeyWordExtract.extractKeyword(dic[name].decode("utf8")).encode("utf8") )

    print name #+ ":" + KeyWordExtract.extractKeyword(dic[name].decode("utf8")) 
    print KeyWordExtract.extractKeyword(dic[name]) 

f.close()
#link = links[0]
#print TCrawler.getSoup(TCrawler.getText(link)).find("h2",id="app-title").text

#print "_".join(jieba.cut(text))
