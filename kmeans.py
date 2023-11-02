# 2次元プロットデータ（3クラス）のデータを読み込んで，k-means法でクラスタリングする
import numpy as np
import matplotlib.pyplot as plt

# 2点間距離を測る関数
def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    dist =  np.sqrt(dist)    
    return dist

# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

#初期値
val0 = np.array([0,0])
val1 = np.array([-0.25,1])
val2 = np.array([0.75,0.25])

dist = [0,0,0]


index = 0
count = 0

i = 0
class0 = []
class1 = []
class2 = []
#クラス分け
while True:
    while index < len(data):
        dist[0] = np.linalg.norm(val0-data[index])
    
        dist[1] = np.linalg.norm(val1-data[index])
    
        dist[2] = np.linalg.norm(val2-data[index])

        minIndex  = dist.index(min(dist))

        if minIndex == 0:
            class0.append(data[index])
        elif minIndex == 1:
            class1.append(data[index])
        elif minIndex == 2:
            class2.append(data[index])
        dist[0] = 0
        dist[1] = 0
        dist[2] = 0
        index += 1

    #比較するために重心を記録
    beforeVal0x = val0[0]
    beforeVal0y = val0[1]
    beforeVal1x = val1[0]
    beforeVal1y = val1[1]
    beforeVal2x = val2[0]
    beforeVal2y = val2[1]
        
    val0x = 0
    val0y = 0
    val1x = 0
    val1y = 0
    val2x = 0
    val2y = 0
    
    #xとyの合計,重心を測る
    size = 0
    while size < len(class0):
        val0x += class0[size][0]
        val0y += class0[size][1]
        size += 1
    size = 0
    while size < len(class1):
        val1x += class1[size][0]
        val1y += class1[size][1]
        size += 1
    size = 0
    while size < len(class2):
        val2x += class2[size][0]
        val2y += class2[size][1]
        size += 1
            
    val0[0] = round(val0x/len(class0),5)
    val0[1] = round(val0y/len(class0),5)
    
    val1[0] = round(val1x/len(class1),5)
    val1[1] = round(val1y/len(class1),5)
   
    val2[0] = round(val2x/len(class2),5)
    val2[1] = round(val2y/len(class2),5)


    print(beforeVal0x,beforeVal0y ,val0)
    print(beforeVal1x,beforeVal1y ,val1)
    print(beforeVal2x,beforeVal2y ,val2)

    if beforeVal0x == val0[0] and beforeVal0y == val0[0]:
        count += 1

    if beforeVal1x == val1[0] and beforeVal1y == val1[0]:
        count += 1

    if beforeVal2x == val2[0] and beforeVal2y == val2[0]:
        count += 1
    if count == 3:
        break
    

#表示
plt.scatter(val0[0],val0[1],marker = "x",color = "r",alpha = 0.5)
plt.scatter(val1[0],val1[1],marker = "x",color = "b",alpha = 0.5)
plt.scatter(val2[0],val2[1],marker = "x",color = "g",alpha = 0.5)
size = 0
while size < len(class0):
    plt.scatter(class0[size][0],class0[size][1],s = 10,color = "r")
    size += 1
size = 0
while size < len(class1):
    plt.scatter(class1[size][0],class1[size][1],s = 10,color = "b")
    size += 1
size = 0
while size < len(class2):
    plt.scatter(class2[size][0],class2[size][1],s = 10,color = "g")
    size += 1

plt.grid()
plt.show()
