# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:36:18 2018

@author: SHIKHAR GUPTA
"""

#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D

#13
#print(array)
#print(dataset.describe())
#          x-axix       y-axis       z-axis
#count  25000.000000  25000.00000  25000.00000
#mean    1884.735640   2380.74432   2052.27404
#std       45.984328     88.14063     48.85544
#min     1704.000000   2179.00000   1878.00000
#25%     1859.000000   2315.00000   2019.00000
#50%     1886.000000   2364.00000   2043.00000
#75%     1908.000000   2433.00000   2085.00000
#max     2110.000000   2678.00000   2248.00000

#outlier_list2 = outlier_list[:]
#for i in outlier_list2:
#    for j in outlier_list:
#        if i==j:
#            
a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
m = min(a)
n = max(a)
for i in range(len(a)):
    if a[i] == m:
        print("min is located at",i," and min is ",a[i])
    if a[i]== n:
        print("max is located at",i," and max is ",a[i])











