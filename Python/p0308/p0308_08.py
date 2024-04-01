import random

a = '123456'
b = '777776'
cnt = 0
for i in range(len(a),0,1):
    if i == 1: continue # 조 는 건너뛰기
    if a[i-1] != b[i-1]:
        break
    else:
        cnt += 1  # 맞는 회수 1증가
if cnt == 0:
    print('완전 꽝입니다.')
if cnt == 1:
    print('6번째 자리가 맞았습니다. 당첨금액 : 1만원')
if cnt == 2:
    print('완전 꽝입니다.')
if cnt == 3:
    print('완전 꽝입니다.')
if cnt == 4:
    print('완전 꽝입니다.')
if cnt == 5:
    print('완전 꽝입니다.')
if cnt == 6:
    print('완전 꽝입니다.')
# 6번째자리가 맞으면 1만원
# 5,6번째자리 10만원
# 4,5,6,번째자리 100만원
# 3456번째자리 1000만원
# 23456번째자리 1억원
# 123456번째자리 10억원
# 1조 100억원
    