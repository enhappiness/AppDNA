import urllib2
#import jieba
from bs4 import BeautifulSoup
import collections


class TCrawler:
    def __init__(self):
        pass
    @staticmethod
    def getText(url):
        return urllib2.urlopen(url).read()

    @staticmethod
    def getSoup(text,lib="html5lib"):
        return BeautifulSoup(text,lib)

    def filter():
        pass

