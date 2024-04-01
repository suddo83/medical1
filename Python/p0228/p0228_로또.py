from random import *

# 1 - 45 까지의 숫자를 넣어서
mynum = []
lotto = []
# 입력을 1 - 45사이의 랜덤한 숫자를 입력을 받음(6개)
# 1 - 45사이의 랜덤한 숫자 6자리 저장
# 4. 입력숫자와 랜덤숫자 비교
# 5. 출력

for i in range(6):
    a = randint(1,45)
    lotto.append(a)
    b = int(input('숫자입력 >> '))
    mynum.append(b)
print(mynum)
print(lotto)

ok = []
for i in range(6):
    if mynum[i] in lotto:
        ok.append(mynum[i])
print('입력한숫자 : {}'.format(mynum))
print('로또숫자 : {}'.format(lotto))
print('당첨된 번호 : {}'.format(ok))


# # 3. 로또 번호 생성하기
l = []
for i in range(1,46):
    l.append(i)
print('로또 숫자 : {}'.format(l))
for i in range(200):
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp],l[0]
for i in range(6):
    lotto.append(l[i])
print('로또 숫자 : {}'.format(l))
