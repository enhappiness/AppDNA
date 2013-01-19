# -*- coding: UTF-8 -*-
import collections
d = collections.defaultdict(lambda:1)

def init(filename='SogouLabDic.dic'):
    f = open(filename,'r')
    result = open("temp",'w')
    total = 0
    while True:
        line = f.readline()
        if not line:
            break
        word,freq = line.split("\t")[0:2]
        total +=int(freq) + 1
        try:
            d[word.decode("gbk")] = int(freq) + 1
        except:
            d[word] = int(freq) + 1
        result.write(word + " : " + freq + "\n")
    f.close()
    result.close()
    d['_t_'] = total


def solve(s):
    l = len(s)
    totalNum = d['_t_']
    #cut sentences into different words
    #m = [i for i in range(0,l+1)]
    #n = [k for k in range(0,i+1)]
    p = [0 for i in range(0,l+1) ] 
    q = [1 for i in range(0,l+1) ] 
    p[0] = 1
    t = [0 for i in range(0,l+1) ] 
    print totalNum
    for i in range(1,l+1):
        #for k in range(0,i):
        for k in range(i - 1 , -1 ,-1):
            wordCount = d[s[k:i]]
            if(wordCount==1):
                continue
            #rate = wordCount / totalNum
            print "i=",i,"k=",k,"wordCound:",wordCount,s[k:i]
            #print "p ",p
            #print "q ",q
            print "t ",t
            if(wordCount * p[k] * q[i] > p[i] * totalNum * q[k]):
                print "--> k=",k
                print "---------------"
                p[i] = p[k] * wordCount
                q[i] *= totalNum 
                t[k] = i
    print t

if __name__ == '__main__':
    init()
    s = '我爱中国'
    s = '他的名字是小明'
    s = '其中最经典就是这部电影了'
    s = s.decode("utf8")
    solve(s)
