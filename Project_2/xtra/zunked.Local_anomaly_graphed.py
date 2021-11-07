import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

########################   CONTROL PARAMETERS   ##############################
zz = 2970    # length of dataset
ds = 1       # downsampling
div = 20     # no. of vertical divisions
Catch = 100  # no of least countinuous max sensor instance to be caught as an anomaly
Cont = 10    # sequences of data to be used to calculate hidden markov model probability
limit = [1000,2500]
###############    training data
train_filename = "000_Et_H_CO_n.csv"

#################  testing data with 1.25 times
#test_filename = "000_Et_H_CO_n_7_1.30_1950_2150.csv"
#test_filename = "000_Et_H_CO_n_7_1.50_1950_2150.csv"
test_filename = "032_Et_H_CO_n_3_1.25_1050_1230.csv"
#test_filename = "032_Et_H_CO_n_3_1.50_1050_1230.csv"
#test_filename = "066_Et_H_CO_n_3_1.25_2200_2450.csv"
#test_filename = "066_Et_H_CO_n_3_1.50_2200_2450.csv"
#test_filename = "098_Et_H_CO_n_2_1.30_1350_1550.csv"
#test_filename = "098_Et_H_CO_n_2_1.50_1350_1550.csv"
#test_filename = "132_Et_H_CO_n_4_1.30_2150_2300.csv"
#test_filename = "132_Et_H_CO_n_4_1.50_2150_2300.csv"
#test_filename = "164_Et_H_CO_n_0_1.25_2450_2600.csv"
#test_filename = "164_Et_H_CO_n_0_1.50_2450_2600.csv"
#test_filename = "164_Et_H_CO_n_6_1.30_1600_1800.csv"
#test_filename = "164_Et_H_CO_n_6_1.50_1600_1800.csv"

# train sensors : collectionn of individual sensor inputs into packets of ds data each

train_dataset = read_csv(train_filename)
train_array = train_dataset.values

a,b,c,d,e,f,g,h = [],[],[],[],[],[],[],[]
sensors = [a,b,c,d,e,f,g,h]
count = 3
sum =0
n=1
for i in sensors:
    while(n<zz and count<11):
        for k in range(ds*(n-1),ds*n):
            sum += train_array[k][count]
        i.append(sum/ds)
        sum=0
        n+=1
    count+=1
    n=1


plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.plot(d)
plt.plot(e)
plt.plot(f)
plt.plot(g)
plt.plot(h)
plt.legend(['1', '2', '3', '4','5','6','7','8'], loc='upper left')
plt.show()
print("Test File Plot")
# test_sensors : collectionn of individual sensor inputs into packets of ds data each

test_dataset = read_csv(test_filename)
test_array = test_dataset.values

aa,bb,cc,dd,ee,ff,gg,hh = [],[],[],[],[],[],[],[]
test_sensors = [aa,bb,cc,dd,ee,ff,gg,hh]
count = 3
sum =0
n=1
for i in test_sensors:
    while(n<zz and count<11):
        for k in range(ds*(n-1),ds*n):
            sum += test_array[k][count]
        i.append(sum/ds)
        sum=0
        n+=1
    count+=1
    n=1


plt.plot(aa)
plt.plot(bb)
plt.plot(cc)
plt.plot(dd)
plt.plot(ee)
plt.plot(ff)
plt.plot(gg)
plt.plot(hh)
plt.legend(['1', '2', '3', '4','5','6','7','8'], loc='upper left')
plt.show()
print("Train File Plot")
################    min max fitting
#for i in range(8):
#    print(min(sensors[i]),max(sensors[i]),"  :  ",min(test_sensors[i]),max(test_sensors[i]))
################    vertical collection of input data into packets

min_train,max_train,min_test,max_test,width_train,width_test = [],[],[],[],[],[]   
mean_train,mean_test = [],[] 
for i in range(8):
    j = sensors[i]
    k = test_sensors[i]
    min_train.append(min(j))
    max_train.append(max(j))
    mean_train.append(np.mean(j))
    width_train.append((max(j)-min(j))/div)
    
    min_test.append(min(k))
    width_test.append((max(k)-min(k))/div) 
    max_test.append(max(k))
    mean_test.append(np.mean(k))

###################### 
m,n,o,p,q,r,s,t = [],[],[],[],[],[],[],[]
train_layer = [m,n,o,p,q,r,s,t]    

mm,nn,oo,pp,qr,rr,ss,tt = [],[],[],[],[],[],[],[]
test_layer = [mm,nn,oo,pp,qr,rr,ss,tt]    

###################          Vertical assingnment/disribution
v = div
for i in range(8):
    j = train_layer[i]
    k = test_layer[i]
    mean_diff = mean_test[i] - mean_train[i]
    m = min_train[i]
    w = width_train[i]
    mm = m - div*w
    for l in sensors[i]: 
        for z in range(v):
            if l >= (m + z*w) and l < (m + (z+1)*w):
                j.append(z+v)
                break
            elif l == (m + v*w):
                j.append(v+v)
                break
    for l in test_sensors[i]:
        for z in range(3*v):
            if l >= (mm + z*w) and l < (mm + (z+1)*w):
                k.append(z)
                break
            elif l == (mm + 3*v*w):
                k.append(v + v + v)
                break
#for i in range(8):
#    print(len(train_layer[i]))
#    print(len(test_layer[i]))

plt.plot(train_layer[0])
plt.plot(train_layer[1])
plt.plot(train_layer[2])
plt.plot(train_layer[3])
plt.plot(train_layer[4])
plt.plot(train_layer[5])
plt.plot(train_layer[6])
plt.plot(train_layer[7])
plt.legend(['1', '2', '3', '4','5','6','7','8'], loc='upper left')
plt.show()            
print("Vertical Assignments of Training Data")

plt.plot(test_layer[0])
plt.plot(test_layer[1])
plt.plot(test_layer[2])
plt.plot(test_layer[3])
plt.plot(test_layer[4])
plt.plot(test_layer[5])
plt.plot(test_layer[6])
plt.plot(test_layer[7])
plt.legend(['1', '2', '3', '4','5','6','7','8'], loc='upper left')
plt.show()
print("Vertical Assignments of Testing Data")
##################   data distribution test
#for i in range(8):
#    print(len(sensors[i]),len(test_sensors[i]),"  :  ",len(train_layer[i]),len(test_layer[i]))
##################   inst list of list and gap array b/w "m" sequence and "mm" for each instance


inst = []
for l in range(2650):
    gap_array = []
    for i in range(8):
        j = train_layer[i]
        k = test_layer[i]
        if (j[l] - k[l]) >= (k[l] - j[l]):
            gap_array += [ j[l] - k[l] ]
        else:
            gap_array += [ k[l] - j[l] ]
    inst += [gap_array]        
###############################
ga,gb,gc,gd,ge,gf,gg,gh = [],[],[],[],[],[],[],[]
gaps = [ga,gb,gc,gd,ge,gf,gg,gh]
n=1
for i in range(8):
    for j in inst:
        gaps[i].append(j[i])

plt.plot(ga)
plt.plot(gb)
plt.plot(gc)
plt.plot(gd)
plt.plot(ge)
plt.plot(gf)
plt.plot(gg)
plt.plot(gh)
plt.legend(['1', '2', '3', '4','5','6','7','8'], loc='upper left')
plt.show()
print("Training And Testing Differnce")
###################   instance check
#print(inst)    
######################    *********    Markov Model   *********   #########################    
###################    emmision matrix probability assignment
emm_prob = []
sensor_max_list = []
for i in inst:
    g_sum=0
    for j in i:
        g_sum += j
    emm_prob.append(8*max(i) - g_sum)
    for k in range(8):
        if max(i) == i[k]:
            sensor_max_list.append(k)
            break
            
###################    normalisation
z = max(emm_prob)
for i in range(len(emm_prob)):
    emm_prob[i] = emm_prob[i]/z                
    
####################  emmision probability check
#print(len(emm_prob),"   ",len(sensor_max_list))
#print(sensor_max_list)
#print(emm_prob)
#plt.plot(emm_prob)
#plt.show(sensor_max_list)
#plt.show()
##############  Obserbation list with "sensor_max_list" and "emm_prob" combined
track = []
Observation = []
temp = []
t = []
for i in range(len(sensor_max_list)):
    if i+1 == len(sensor_max_list):
        temp.append([sensor_max_list[i],emm_prob[i]])
        Observation += [temp]
        t.append(i)
        track += [t]
    else:
        if sensor_max_list[i] == sensor_max_list[i+1]:
            temp.append([sensor_max_list[i],emm_prob[i]])
            t.append(i)
            
        else:
            temp.append([sensor_max_list[i],emm_prob[i]])
            Observation += [temp]
            temp = []
            t.append(i)
            track += [t]
            t = []

#####################    error check
#print(len(track),len(sensor_max_list),len(emm_prob),len(Observation))
#print(Observation)
#print(track)
            
###############    hidden markov model transition matrix and initial state matrix
pi = 0.5 
A = [1,0.5]
#B = []
#for i in emm_prob:
#    B += [[i,1-i]]
    
###############    probability of observation for each block(10 instance each) of data
P = []
for i in Observation:
    if len(i)>Catch:
        Ps = []
        n = len(i)//Cont   # n = len(i)-Catch 
        Ps.append( i[0][0] ) 
        for c in range(n):
            p = ( i[c*Cont][1] * pi )
            for j in range(1,Cont-1):
                p = p * ( i[c*Cont+j][1]) * A[0]
            Ps.append( p )               
        P += [Ps]
    
################
#print(P)
#print(len(Observation),len(tr))
#print(len(P))
#print(tr)
#print(len(track))

###########################################################    Final Selection
count    = []     # Location Track of Anomaly
A_sensor = []     # Anomalous Sensor Number (0-7)
n_CAB    = []     # No of Countinious Anomalous Blocks
A_prob   = []     # Probability of anomalous sequence
for i in P:
    A_sensor.append(i[0])
    n_CAB.append(len(i)-1)
    c = len(i)
    A_prob_s = 0
    for j in range(1,c):
        A_prob_s += i[j]
    A_prob += [ A_prob_s/(c-1) ] 

for i in range(len(track)):
    k = track[i][0]
    if len(track[i])>Catch:
        count += [k]
        
##########################################################     Print it out
#print(count)
#print(A_sensor)
#print(n_CAB)
#print(A_prob)

print("Seq.   Track   Sensor no.   Intensity   Probability of Anomaly")
for i in range(len(A_sensor)):
    print(" %-5d %-7d %-12d %-14d %-12.10f"%(i+1,count[i],A_sensor[i],n_CAB[i],A_prob[i]))



