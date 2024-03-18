import random

c_number = [0]*13
for i in range(13):
    c_number[i] += i+1
# print(c_number)
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]


# 랜덤으로 2개를 숫자를 뽑아서 출력하시오.
# 랜덤숫자 : 2 -> 1번방에 있습니다.
# 랜덤숫자 : 9 -> 8번방에 있습니다.
# 큰수 : 9, 작은수 : 2
s_number = random.sample(c_number,k=2)
print(s_number)
for i in s_number:
    loc = c_number.index(i)
    print(f'랜덤숫자 :{i} -> {loc}번방에 있습니다.')

h1 = max(s_number)
l1 = min(s_number)
print(f'큰수 :{h1}, 작은수 :{l1}')


