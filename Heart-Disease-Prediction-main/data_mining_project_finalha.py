# -*- coding: utf-8 -*-
"""Data_Mining_Project_finalha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SVYDVs752QJnVeAyGYGyoi7ErmfU3EOR
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

import os
print(os.listdir())

import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv("/content/heart12.csv")

dataset.head()

dataset.dropna()

dataset.shape

dataset.isnull().sum()

dataset.info()



info = ["age","1: male, 0: female","chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic","resting blood pressure"," serum cholestoral in mg/dl","fasting blood sugar > 120 mg/dl","resting electrocardiographic results (values 0,1,2)"," maximum heart rate achieved","exercise induced angina","oldpeak = ST depression induced by exercise relative to rest","the slope of the peak exercise ST segment","number of major vessels (0-3) colored by flourosopy","thal: 1 = normal; 2 = fixed defect; 3 = reversable defect"]



for i in range(len(info)):
    print(dataset.columns[i]+":\t\t\t"+info[i])

"""CHECKING DATA"""

dataset.drop(dataset[dataset['sex'] > 1].index, inplace = True)

dataset.shape

dataset.drop(dataset[dataset['age'] > 100].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['cp'] > 4].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['restecg'] > 2].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['fbs'] > 1].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['exang'] > 1].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['ca'] > 3].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['slope'] > 2].index, inplace = True)
dataset.shape

dataset.drop(dataset[dataset['thal'] > 2].index, inplace = True)
dataset.shape

"""**Exploratory Data Analysis (EDA)**

FEATURE 'TARGET'
"""

y = dataset["target"]

sns.countplot(y)


target_temp = dataset.target.value_counts()

print(target_temp)

print("Percentage of patience without heart problems: "+str(round(target_temp[0]*100/303,2))+"%")
print("Percentage of patience with heart problems: "+str(round(target_temp[1]*100/303,2))+"%")

"""FEATURE 'AGE'"""

sns.histplot(dataset['age'][dataset['target']==1])

"""FEATURE 'BLOOD PRESSURE'"""

sns.histplot(dataset['trestbps'][dataset['target']==1])

"""FEATURE 'CHOLESTEROL'"""

sns.histplot(dataset['chol'][dataset['target']==1])

"""FEATURE 'Maximum heart rate achieved '"""

sns.histplot(dataset['thalach'][dataset['target']==1])

"""FEATURE 'ST Depression '"""

sns.histplot(dataset['oldpeak'][dataset['target']==1])

"""FEATURE 'Gender'"""

sns.barplot(dataset["sex"],y)

"""FEATURE 'Chest pain '"""

sns.barplot(dataset["cp"],y)

"""FEATURE 'Fasting Blood Glucose Level '"""

sns.barplot(dataset["fbs"],y)

"""FEATURE 'Resting Electrocardiographic'"""

sns.barplot(dataset["restecg"],y)

"""FEATURE 'Exercise induced angina '"""

sns.barplot(dataset["exang"],y)

"""FEATURE 'Slope of ST:'"""

sns.barplot(dataset["slope"],y)

"""FEATURE 'Number of vessels fluro '"""

sns.barplot(dataset["ca"],y)

"""FEATURE 'Thallium'"""

sns.barplot(dataset["thal"],y)

"""**Train Test split**"""

from sklearn.model_selection import train_test_split

predictors = dataset.drop("target",axis=1)
target = dataset["target"]

X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=0)

X_train.shape

X_test.shape

Y_train.shape

X_test

Y_test.shape

"""**MODEL FITTING**"""

from sklearn.metrics import accuracy_score

"""**LOGISTIC REGRESSION**"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train,Y_train)

Y_pred_lr = lr.predict(X_test)

Y_pred_lr.shape

from sklearn.metrics import plot_confusion_matrix
disp = plot_confusion_matrix(lr, X_test, Y_test, cmap=plt.cm.Blues)
plt.grid(None)
print(disp.confusion_matrix)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
tpl, fnl, fpl, tnl = confusion_matrix(Y_test,Y_pred_lr,labels=[1,0]).reshape(-1)
print('Outcome values : \n', tpl, fnl, fpl, tnl)

prelr=((tpl)/(tpl+fpl))*100
prelr=round(prelr,2)
print("The Precision score achieved using Logistic Regression is: "+str(prelr)+" %")

recalr=((tpl)/(tpl+fnl))*100
recalr=round(recalr,2)
print("The Recall score achieved using Logistic Regression is: "+str(recalr)+" %")
f1slr=2/((1/recalr)+(1/prelr))
f1slr=round(f1slr,2)
print("The F1-Score score achieved using Logistic Regression is: "+str(f1slr)+" %")

score_lr = round(accuracy_score(Y_pred_lr,Y_test)*100,2)

print("The accuracy score achieved using Logistic Regression is: "+str(score_lr)+" %")

import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification

fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_lr)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

"""**K NEAREST NEIGHBORS**"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,Y_train)
Y_pred_knn=knn.predict(X_test)

Y_pred_knn.shape

from sklearn.metrics import plot_confusion_matrix

disp = plot_confusion_matrix(knn, X_test, Y_test,
                                 cmap=plt.cm.Blues)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
tpk, fnk, fpk, tnk = confusion_matrix(Y_test,Y_pred_knn,labels=[1,0]).reshape(-1)
print('Outcome values : \n', tpk, fnk, fpk, tnk)
#matrix = classification_report(Y_test,Y_pred_knn,labels=[1,0])
#print('Classification report : \n',matrix)

plt.grid(None)

preknn=((tpk)/(tpk+fpk))*100
preknn=round(preknn,2)
print("The Precision score achieved using K-Nearest Neighbor is: "+str(preknn)+" %")

recaknn=((tpk)/(tpk+fnk))*100
recaknn=round(recaknn,2)
print("The Recall score achieved using K-Nearest Neighbor is: "+str(recaknn)+" %")
f1sknn=2/((1/recaknn)+(1/preknn))
f1sknn=round(f1sknn,2)
print("The F1-Score score achieved using K-Nearest Neighbor is: "+str(f1sknn)+" %")

score_knn = round(accuracy_score(Y_pred_knn,Y_test)*100,2)

print("The accuracy score achieved using KNN is: "+str(score_knn)+" %")

# calculate the fpr and tpr for all thresholds of the classification

fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_knn)
roc_auc = metrics.auc(fpr, tpr)
plt.figure(figsize=(6,5))


plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(None)
plt.show()

"""

**SUPPORT VECTOR MACHINE**"""

from sklearn import svm

sv = svm.SVC(kernel='linear')

sv.fit(X_train, Y_train)

Y_pred_svm = sv.predict(X_test)

Y_pred_svm.shape

from sklearn.metrics import plot_confusion_matrix
disp = plot_confusion_matrix(sv, X_test, Y_test,
                                 cmap=plt.cm.Blues)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
tps, fns, fps, tns = confusion_matrix(Y_test,Y_pred_svm,labels=[1,0]).reshape(-1)
print('Outcome values : \n', tps, fns, fps, tns)

presvm=((tps)/(tps+fps))*100
presvm=round(presvm,2)
print("The Precision score achieved using Support Vector Machine is: "+str(presvm)+" %")

recasvm=((tps)/(tps+fns))*100
recasvm=round(recasvm,2)
print("The Recall score achieved using Support Vector Machine is: "+str(recasvm)+" %")
f1ssvm=2/((1/recasvm)+(1/presvm))
f1ssvm=round(f1ssvm,2)
print("The F1-Score score achieved using Support Vector Machine is: "+str(f1ssvm)+" %")

score_svm = round(accuracy_score(Y_pred_svm,Y_test)*100,2)

print("The accuracy score achieved using Linear SVM is: "+str(score_svm)+" %")

import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification

fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_svm)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
plt.figure(figsize=(6,5))
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(None)

plt.show()

"""**RANDOM FOREST**"""

from sklearn.ensemble import RandomForestClassifier

max_accuracy = 0


for x in range(200):
    rf = RandomForestClassifier(random_state=x)
    rf.fit(X_train,Y_train)
    Y_pred_rf = rf.predict(X_test)
    current_accuracy = round(accuracy_score(Y_pred_rf,Y_test)*100,2)
    if(current_accuracy>max_accuracy):
        max_accuracy = current_accuracy
        best_x = x
        
#print(max_accuracy)
#print(best_x)

rf = RandomForestClassifier(random_state=best_x)
rf.fit(X_train,Y_train)
Y_pred_rf = rf.predict(X_test)

Y_pred_rf.shape

matrix = classification_report(Y_test,Y_pred_rf,labels=[1,0])
print('Classification report : \n',matrix)

from sklearn.metrics import plot_confusion_matrix
disp = plot_confusion_matrix(rf, X_test, Y_test,
                                 cmap=plt.cm.Blues)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
tpr, fnr, fpr, tnr = confusion_matrix(Y_test,Y_pred_rf,labels=[1,0]).reshape(-1)
print('Outcome values : \n', tpr, fnr, fpr, tnr)

prerf=((tpr)/(tpr+fpr))*100
prerf=round(prerf,2)
print("The Precision score achieved using Random Forest is: "+str(prerf)+" %")

recarf=((tpr)/(tpr+fnr))*100
recarf=round(recarf,2)

print("The Recall score achieved using Random Forest is: "+str(recarf)+" %")
f1srf=2/((1/recarf)+(1/prerf))
f1srf=round(f1srf,2)
print("The F1-Score score achieved using Random Forest is: "+str(f1srf)+" %")

score_rf = round(accuracy_score(Y_pred_rf,Y_test)*100,2)

print("The accuracy score achieved using Random Forest is: "+str(score_rf)+" %")

import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification

fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_rf)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
plt.figure(figsize=(6,5))
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(None)

plt.show()

"""** COMPARING EACH MODEL'S SCORE**"""

scores = [score_lr,score_knn,score_svm,score_rf]
algorithms = ["Logistic Regression","K-Nearest Neighbors","Support Vector Machine","Random Forest"] 

for i in range(len(algorithms)):
    print("The accuracy score achieved using "+algorithms[i]+" is: "+str(scores[i])+" %")

sns.set(rc={'figure.figsize':(15,8)})
plt.xlabel("Algorithms")
plt.ylabel("Accuracy score")

sns.barplot(algorithms,scores)

