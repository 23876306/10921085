import sys
import numpy as np
import random as rand

np.zeros((2, 3))                #建立一個2x3的陣列
np.ones((2, 3, 4))              #建立一個2x3x4全為1的陣列
np.arange(1, 10, 2)             #建立一個由1開始，不超過10，間隔均為2的均勻數值陣列
np.linspace(0, 10, 5)          #建立一個由0-10之間，均勻的5個數值陣列
x1 = np.full((3, 2), 8)              #建立一個3x2且全為8的陣列


a = np.array([1, 2, 3, 4])                                                              #一維陣列
#print(a)

b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype = float)                           #二維陣列
#print(b)

c = np.array([[(5, 1.4, 3.5, 4.5)], [(5, 6, 7, 8)], [(1, 4.4, 11, 3.7)]], dtype = float)#三維陣列
#print(c)

d = np.random.randint(2, 135, (2, 3))                                                   #建立一個隨機由2-135的2x3陣列
#print(d)

e = d.reshape(1, 6)
#print(e)

fileName = "output_1.npy"
#with open(fileName, "wb") as fp:
    #np.save(fp, x1)


#-------------------------------我是分隔線----------------------------
data = list(input())
print(data)
rand.seed(1980)
rand.shuffle(data)                      #shuffle:打亂資料
print("".join(data))