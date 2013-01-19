import sys
from Crawler import TCrawler
sys.path.append("../Analyse")
#import extract_keyword

f = open("result.txt",r)

print TCrawler.getText("http://baidu.com")
