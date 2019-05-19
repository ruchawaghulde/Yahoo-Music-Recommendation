#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


d1 = pd.read_csv("~/Desktop/Ensemble submission collection/submission_file.txt")
d2 = pd.read_csv("~/Desktop/Ensemble submission collection/Submission1.csv")
d3 = pd.read_csv("~/Desktop/Ensemble submission collection/Submission3.csv")
d4 = pd.read_csv("~/Desktop/Ensemble submission collection/Submission4.csv")
d5 = pd.read_csv("~/Desktop/Ensemble submission collection/submission5.txt")



data1 = d1.drop(columns=['TrackID'], axis=1)
data2 = d2.drop(columns=['TrackID'], axis=1)
data3 = d3.drop(columns=['trackID'], axis=1)
data4 = d4.drop(columns=['TrackID'], axis=1)
data5 = d5.drop(columns=['TrackID'], axis=1)

X = pd.DataFrame()

X['A'] = data1['Predictor']
X['B'] = data2['Predictor']
X['C'] = data3['Predictor']
X['D'] = data4['Predictor']
X['E'] = data5['Predictor']

#print(X)
X_new = X.replace(0, -1)
#print(X_new)

X_transpose = pd.DataFrame.transpose(X_new)
#print(X_transpose)

X2 = X_transpose.values.tolist()
X1 = X_new.values.tolist()
result = ([0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0])

for i in range(len(X2)):
    for j in range(len(X1[0])):
        for k in range (len(X1)):
            result[i][j] += X2[i][k] * X1[k][j]
for r in result:
    print(r)

rinv = np.linalg.inv(result)

#print(rinv)


score1 = 120000 * ((2 * 0.75670) - 1)
score2 = 120000 * ((2 * 0.57437) - 1)
score3 = 120000 * ((2 * 0.51657) - 1)
score4 = 120000 * ((2 * 0.49835) - 1)
score5 = 120000 * ((2 * 0.59865) - 1)

XTY = [[score1], [score2], [score3], [score4], [score5]]

#print(XTY)


coeff = ([0],[0],[0],[0],[0])
list = []
for l in range(len(rinv)):
    for m in range(len(XTY[0])):
        for n in range (len(XTY)):
            coeff[l][m] += rinv[l][n] * XTY[n][m]
for a in coeff:
    print(a)
    for u in a:
        list.append(u)
print(list)
print(X_new)

X_new['A'] = X_new['A'] * list[0]
X_new['B'] = X_new['B'] * list[1]
X_new['C'] = X_new['C'] * list[2]
X_new['D'] = X_new['D'] * list[3]
X_new['E'] = X_new['E'] * list[4]

y = pd.DataFrame()
y['Output'] = X_new['A'] + X_new['B'] + X_new['C'] + X_new['D'] + X_new['E']
print(y)

final = pd.read_csv("~/Desktop/submission_file.txt")

final = final.drop(columns=['Predictor'], axis=1)

final['Predictor'] = y['Output']
print(final)


final1 = final

final2 = final1.head(n=6)

final3 = final2.nlargest(3, ['Predictor'])

l = final3.index.values
l

final4 = final

final4

i = 0
j = 6
while i <119994 and j <120000:
    final4 = final[i:j]
    final3 = final4.nlargest(3, ['Predictor'])
    l = final3.index.values
    for k in l:
        final['Predictor'][k] = 1
    i = i+6
    j = j+6

final.to_csv("ensemble.csv")


e = pd.read_csv("~/Desktop/ensemble.csv")

f = e['Predictor']

f = list(f)

for n, i in enumerate(f):
       if i != 1:
          f[n] = 0

e['Predictor'] = f

e = e.drop(columns=['Unnamed: 0'], axis=1)


e.to_csv("ensemble1.csv")
