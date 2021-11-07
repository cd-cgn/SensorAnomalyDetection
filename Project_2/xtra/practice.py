# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:06:09 2018

@author: SHIKHAR GUPTA
"""
from sklearn import linear_model
import matplotlib
import matplotlib.pyplot as plt
from pandas import read_csv
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

train_filename = "000_Et_H_CO_n.csv"
train_dataset = read_csv(train_filename)
train_array = train_dataset.values

a,b,c,d,e,f,g,h = [],[],[],[],[],[],[],[]
sensors = [a,b,c,d,e,f,g,h]
count = 3
sum =0
for i in sensors:
    while(n<297 and count<11):
        for k in range(10*(n-1),10*n):
            sum += train_array[k][count]
        i.append(sum/10)
        sum=0
        n+=1
    count+=1
    n=1


## 2 step process / other way 
#sensors = [a,b,c,d,e,f,g,h]
#count = 3
#for i in sensors:
#    for j in train_array:
#        i.append([j[count]])
#    count +=1
##print(a)    
#aa,bb,cc,dd,ee,ff,gg,hh = [],[],[],[],[],[],[],[]
#
#packets = [aa,bb,cc,dd,ee,ff,gg,hh]
#sum = 0
#for i in sensors:
#    for j in packets:
#        n=1
#        while(n<297):
#            for k in range(10*(n-1),10*n):
#                sum += i[k][0]    
#            j.append(sum/10)
#            n+=1
#            sum = 0    