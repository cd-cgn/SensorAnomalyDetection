#from sklearn import linear_model
#import matplotlib
#import matplotlib.pyplot as plt
from pandas import read_csv
#from mpl_toolkits.mplot3d import Axes3D

test_filename = "032_Et_H_CO_n.csv"
test_dataset = read_csv(test_filename)
test_array = test_dataset.values

# collectionn of individual sensor inputs into packets of 10 data each
#################  testing data
aa,bb,cc,dd,ee,ff,gg,hh = [],[],[],[],[],[],[],[]
test_sensors = [aa,bb,cc,dd,ee,ff,gg,hh]
count = 3
sum =0
n=1
for i in test_sensors:
    while(n<297 and count<11):
        for k in range(10*(n-1),10*n):
            sum += test_array[k][count]
        i.append(sum/10)
        sum=0
        n+=1
    count+=1
    n=1
    
###############    training data
train_filename = "000_Et_H_CO_n.csv"
train_dataset = read_csv(train_filename)
train_array = train_dataset.values

##############    collectionn of individual sensor inputs into packets of 10 data each
a,b,c,d,e,f,g,h = [],[],[],[],[],[],[],[]
sensors = [a,b,c,d,e,f,g,h]
count = 3
sum =0
n=1
for i in sensors:
    while(n<297 and count<11):
        for k in range(10*(n-1),10*n):
            sum += train_array[k][count]
        i.append(sum/10)
        sum=0
        n+=1
    count+=1
    n=1

################    min max fitting
#for i in range(8):
#    print(min(sensors[i]),max(sensors[i]),"  :  ",min(test_sensors[i]),max(test_sensors[i]))

################    vertical collection of input data into packets
minimum,maximum,width = [],[],[]    
for i in range(8):
    j = sensors[i]
    k = test_sensors[i]
    for l in range(297):
        if min(j)<min(k):
            m = min(j)
        else:
            m = min(k)
    for l in range(297):
        if max(j)>max(k):
            n = max(j)
        else:
            n = max(k)
    div = 12
    minimum.append(m)
    maximum.append(n)
    w = (n - m)/div
    width.append(w) 

#print(minimum)
#print(maximum)
#print(width)

###################### 
m,n,o,p,q,r,s,t = [],[],[],[],[],[],[],[]
train_layer = [m,n,o,p,q,r,s,t]    

mm,nn,oo,pp,qr,rr,ss,tt = [],[],[],[],[],[],[],[]
test_layer = [mm,nn,oo,pp,qr,rr,ss,tt]    

for i in range(8):
    j = train_layer[i]
    k = test_layer[i]
    for l in sensors[i]:
        for n in range(12):
            if l >= (minimum[i] + n*width[i]) and l < (minimum[i] + (n+1)*width[i]):
                j.append(n)
    for l in test_sensors[i]:
        for n in range(12):
            if l >= (minimum[i] + n*width[i]) and l < (minimum[i] + (n+1)*width[i]):
                k.append(n)           

##################   data distribution test
#for i in range(8):
#    print(len(sensors[i]),len(test_sensors[i]),"  :  ",len(train_layer[i]),len(test_layer[i]))

##################   inst list of list and gap array b/w "m" sequence and "mm" for each instance
inst = [] 
for l in range(294):
    gap_array = []
    for i in range(8):
        j = train_layer[i]
        k = test_layer[i]
        if (j[l] - k[l]) >= (k[l] - j[l]):
            gap_array += [ j[l] - k[l] ]
        else:
            gap_array += [ k[l] - j[l] ]
    inst += [gap_array]        

###################   instance check
#print(inst)
    
###################    emmision matrix probability assignment
emm_prob = []
for i in inst:
    g_sum=0
    for j in i:
        g_sum += j
    emm_prob.append(8*max(i) - g_sum)

###################    normalisation
z = max(emm_prob)
for i in range(len(emm_prob)):
    emm_prob[i] = emm_prob[i]/z
    
####################  emmision probability check
#print(emm_prob)

###############    hidden markov model transition matrix and initial state matrix
###############    [A = 0, NA = 1]
pi = [0,1] 
A = [[1,0.5],[0,0.5]]
B = []
for i in emm_prob:
    B += [[i,1-i]]

##############    markov model data check
#print(pi,A,B)

##############    anomaly sequence detection















