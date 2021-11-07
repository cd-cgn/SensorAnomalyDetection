# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:16:43 2018

@author: SHIKHAR GUPTA
"""

from pandas import read_csv
#from mpl_toolkits.mplot3d import Axes3D

filename = "1_4_anomaly_detection.csv"
names = ["x-axix","y-axis","z-axis"]
dataset = read_csv(filename,names = names)
array = dataset.values
#print(array)
print(dataset.describe())