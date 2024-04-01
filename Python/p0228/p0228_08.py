from random import *

# 1. 변수선언
lotto = []
mynum = []

# 2. 입력받은 숫자 6개 :

# 3. 로또 번호 생성하기
l = [1,2,3,4,5,6,7,8,9,10]

for i in range(50):
    tmp = randint(0,9) # 0번방 - 9번방까지 랜덤한 숫자를 생성
    l[0],l[tmp] = 1[tmp],l[0]
print(l)

for i in range(6):
    lotto.append(l[i])
print(lotto)