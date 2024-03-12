con  = ['미국','영국','일본','중국','스페인']

# 영국, 중국의 위치를 바꿔보세요
con[1],con[3] = con[3],con[1]
print(con)

from random import *
n1 = [1,2,3,4,5,6,7,8,9,10]

for i in range(3):
    tmp = randint(0,9)
    n1[0],n1[tmp] = n1[tmp],n1[0]
    print(tmp)
    print(n1)