import numpy as np
import pandas as pd
import xlrd
data_3=pd.read_csv("实验双电极.csv",header=None)
ex=data_3.values.tolist()
ex_3=np.zeros([len(ex),len(ex[0])])
ex_3=ex

'''data_32=pd.read_csv("理论双电极.csv",header=None)
th=data_32.values.tolist()
th_3=np.zeros([len(th),len(th[0])])
th_3=th
er_3=0
for i in range(len(th_3)):
    for j in range(len(th_3[0])):
        pass
er_3+=th_3[i][j]'''
f=open('双电极修正2.txt','r')
lines=f.readlines()
m=len(lines)
print('height=',m)
n=len(lines[0].split(' '))
print('width=',n)
I=np.zeros((m,n-1),dtype=float)

i=0
for line in lines:
    list=line.strip('\n').split('\t')

    I[i]=list[0:n]
    i+=1

er_3=0
rer_3=0
Er_3=np.zeros((m,n))
print(len(I[0]))
for i in range(len(ex_3)):
    for j in range(len(ex_3[0])):
        Er_3[i][j]=ex_3[i][j]-I[i][j]
        er_3+=abs(ex_3[i][j]-I[i][j])
        rer_3+=abs(Er_3[i][j]/ex_3[i][j])
print('双电极绝对',er_3/(106*106))
print('双电极相对',rer_3/(106*106))
U_1=11.7
U_2=0.8
a=0.305#电极半径
R=10
r=np.linspace(a,9,421)
U=np.zeros(421)
U=-(U_1-U_2)/np.log(a/R)*np.log(R/r)+U_2


f=open('圆柱实验.txt','r')
lines=f.readlines()
m=len(lines)
print('height=',m)
n=len(lines[0].split(' '))
print('width=',n)
U_r=np.zeros((m,n-1),dtype=float)

i=0
for line in lines:
    list=line.strip('\n').split('\t')

    U_r[i]=list[0:n]
    i+=1
er_2=0
rer_2=0
Er_2=np.zeros((m,n))
print(len(U_r[0]))
for i in range(len(U)):
    Er_2[0][i]=U[i]+U_r[0][i]
    er_2+=abs(U[i]+U_r[0][i])
    rer_2+=abs(Er_2[0][i]/U_r[0][i])
print('圆柱绝对',er_2/421)
print('圆柱相对',rer_2/421)



U_1=11.9
U_2=1.3

s=24.4
x=np.linspace(0,24.5,1175)
V=np.zeros(1175)
V=(U_1-U_2)/s*(s-x)+U_2

f=open('平行板.txt','r')
lines=f.readlines()
m=len(lines)
print('height=',m)
n=len(lines[0].split(' '))
print('width=',n)
U_x=np.zeros((m,n-1),dtype=float)

i=0
for line in lines:
    list=line.strip('\n').split('\t')

    U_x[i]=list[0:n]
    i+=1
er_1=0
rer_1=0
Er_1=np.zeros((m,n))
print(V)
for i in range(len(V)):
    Er_1[0][i]=V[i]-U_x[0][i]
    er_1+=abs(V[i]-U_x[0][i])
    rer_1+=abs(Er_1[0][i]/U_x[0][i])
print('平行板绝对',er_1/421)
print('平行板相对',rer_1/421)