
from sklearn import linear_model
import matplotlib
import matplotlib.pyplot as plt
from pandas import read_csv
from mpl_toolkits.mplot3d import Axes3D


filename = "anomaly_detection_train.csv"
names = ["x-axix","y-axis","z-axis"]
dataset = read_csv(filename,names = names)
array = dataset.values


X = []
Y = []
Z = []
for i in array:
    X.append([i[0]])
    Y.append([i[1]])
    Z.append([i[2]])
    

model_X = linear_model.LinearRegression()
model_X.fit(X,Y)
linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
model_Y = linear_model.LinearRegression()
model_Y.fit(Y,Z)
linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
model_Z = linear_model.LinearRegression()
model_Z.fit(Z,X)
linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)


test_filename = "anomaly_detection_ test.csv"
test_dataset = read_csv(test_filename,names = names)
test_array = test_dataset.values

outlier_list = []
n=1
count = 0
for instance in test_array:
#    print(instance)
    result_Y = model_X.predict(instance[0])
    result_Z = model_Y.predict(instance[1])
    result_X = model_Z.predict(instance[2])
    if result_X > 2110*(.92) or result_X < 1704*(1.05):
        print("Outlier Detected at instance ",n," in value",instance[2]," of Z-axis ")
        #print("Expected X at",result_X)
        count+=1
        outlier_list.append(n)
    if result_Y > 2678*(.92) or result_Y < 2179*(1.05):
        print("Outlier Detected at instance ",n," in value",instance[0]," of X-axis ")
        #print("Expexted Y at",result_Y)
        count+=1
        outlier_list.append(n)
    if result_Z > 2248*(.92) or result_Z < 1878*(1.05):
        print("Outlier Detected at instance ",n," in value",instance[1]," of Y-axis ")
        #print("Expexted Z at",result_Z)
        count+=1
        outlier_list.append(n)
    n += 1

if count>0:
    print(count," anomalies detected")
if n>25000:
    print("No anomaly detected")

matplotlib.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
	
ax.scatter(X,Y,Z, c='b', marker='.')
    
X_test = []
Y_test = []
Z_test = []
for i in test_array:
    X_test.append([i[0]])
    Y_test.append([i[1]])
    Z_test.append([i[2]])

matplotlib.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X_test-Axis')
ax.set_ylabel('Y_test-Axis')
ax.set_zlabel('Z_test-Axis')
ax.scatter(X_test,Y_test,Z_test, c='r', marker='.')

plt.show()
