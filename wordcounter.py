#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:06:00 2023
统计文章词频
@author: jimyu
"""
import jieba
import chardet
import docx

# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def getText(filename):
    txt=open(filename,'r',encoding=get_encoding(filename)).read()
    #txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~\'':
        txt=txt.replace(ch,' ')
    return txt

def getDocx(filename):
    file=docx.Document(filename)
    txt=""
    for para in file.paragraphs:
        txt+=para.text
    return txt


def counterword(txt):
    #排除词，根据第一次运行结果，手工维护。
    excludes={'这样','一个','你们','自己','就是','','',''}

    txtWords=''
    words=jieba.lcut(txt)
    counts={}
    for word in list(words):
        if len(word)==1:
            continue
        elif word == '诸葛亮' or word == '孔明曰':
            rword = '孔明'
        else:
            rword=word
            
        counts[rword]=counts.get(rword,0)+1
    
    #删除排除词
    for word in excludes:
        if word in counts:
            del counts[word]
        
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    #print(items[:9])
    for i in range(50):
        word,count = items[i]
        txtWords+="#{:<3}:{:>10}\t{:<4}\n".format(i+1,word,count)
        #print("#{:<3}:{:>10}\t{:<4}".format(i+1,word,count))
    return txtWords
    
def process(filename):
    txt=getDocx(filename)
    cntWords=counterword(txt)
    f=open('词频'+filename+'.txt','w')
    f.write(cntWords)
    f.close()
       

filename="001 第一篇.txt"
print(get_encoding(filename))
#关联名称
sameWords={
    '孔明':'诸葛亮,孔明曰' ,
    '关羽':'关公,云长' 
    }

#txt=getText(filename)
#filename="《话在肉身显现》 GBK 20221230.docx"
process("《话在肉身显现》 GBK 20221230.docx")
process("1.《实行真理一百七十条原则》20210711.docx")
#process("0.神的交通1-220篇.docx")
process("2.《信神必须实行的二百条真理》20210711.docx")
process("3、《话在肉身显现》中文简体-A4-20201130.docx")
process("4.新版 基督的座谈纪要（合交）.docx")
process("5、弟兄交通（1-200）.docx")
process("6.弟兄讲道（201-240）.docx")

