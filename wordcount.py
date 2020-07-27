# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:03:19 2020

@author: Arushi Gupta
"""

import re
file = open("dog.txt","r")

l=file.read()
l=re.sub("[:,.?()#$]","",l).split()

d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
for k,v in d.items():
    print(k," " , v, "times")
    
    file.close()
    