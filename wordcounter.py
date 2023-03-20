#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:06:00 2023
统计文章词频
@author: jimyu
"""
import jieba

def getText():
    txt=open("../files/threekingdoms.txt",'r',encoding='utf-8').read()
    #txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~\'':
        txt=txt.replace(ch,' ')
    return txt

#排除词，根据第一次运行结果，手工维护。
excludes={'将军','却说'}
#关联名称
sameWords={
    '孔明':'诸葛亮,孔明曰' ,
    '关羽':'关公,云长' 
    }
txt=getText()

words=jieba.lcut(txt)
counts={}
for word in list(words):
    if len(word)==1:
        continue
    elif word == '诸葛亮' or word == '孔明曰':
        rword = '孔明'
    else:
        rword=word
        
    counts[word]=counts.get(word,0)+1

#删除排除词
for word in excludes:
    del counts[word]
    
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
#print(items[:9])
for i in range(20):
    word,count = items[i]
    print("#{:<3}:{:>10}\t{:<4}".format(i+1,word,count))
    
    



    
    