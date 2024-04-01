from random import *

lotto = []
mynum = []
for i in range(6):
    n2 = int(input('숫자입력 >> '))
    mynum.append(n2)
print(mynum)

for i in range(6):
    n1 = randint(1,45)
    lotto.append(n1)
print(lotto)