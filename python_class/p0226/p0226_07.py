# ramdom 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 10이하의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 10이하의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 10이하의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

# 해보세요
# 1~10사이의 숫자를 입력받아서 변수1
# 변수2 1-10사이의 랜덤한 숫자
# 랜덤한 숫자와 비교해 같으면 [당첨]
# 다르면 [랜덤숫자는 {}로 일치하지 않습니다]

a = int(input('1에서 10사이의 숫자입력 >> '))
b = randint(1,10)
if 1 <= a <= 10:
    if a == b:
        print('당첨')
    else:
        print('랜덤숫자는 {} 일치하지 않습니다'.format(b))
else:
    print('범위초과')
