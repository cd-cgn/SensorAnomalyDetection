# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 20:43:27 2018

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


sensors = ['a','b','c','d','e','f','g','h']
count = 3

sum =0
for i in sensors:
    for n in range(100):
        i.append(n)


#for j in train_array:
#    print(j[count])