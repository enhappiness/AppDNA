# -*- coding: UTF-8 -*-
import sys
import jieba
import jieba.analyse

class KeyWordExtract:
    def __init__(self):
        pass
    @staticmethod
    def extractKeyword(text,topK = 10):
        return " ".join(jieba.analyse.extract_tags(text,topK))

#print KeyWordExtract.extractKeyword("适远是一个积极向上的好学生".decode("utf8"))
s = """身在户外、要与朋友吃饭,却不知附近是否有合适餐馆? 
坐在餐馆,想知道这家餐厅都有哪些美味的推荐菜? 
出门旅游,想找当地最具特色的美食? 

现在通过大众点评网app,以上问题即可迎刃而解了。 

主要功能: 
─ 随时随地查找美食、休闲娱乐、酒店等各种商家 
─ GPS定位自动搜索周边各类商户,省时省力 
─ 提供商户电话、地址地图、客观点评等全面信息 
─ 北京上海等八大城市优惠券免费下载,折扣不断 
─ 给力团购:吃喝玩乐、低至一折。高品质值得信赖"""
s = s.decode("utf-8")
print KeyWordExtract.extractKeyword(s)


