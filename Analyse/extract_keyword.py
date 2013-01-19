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
