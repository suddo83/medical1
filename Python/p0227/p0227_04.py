""" 반복문 - for, while

fof 변수 in 반복가능한데이터:
    수행문
    
for 카운터변수 in range(시작값, 끝값+1, 증감값)
    수행문
"""

# for i in range(0,10,1): # 0,1,2,3,4,5,6,7,9
#     print('수행문입니다.')
    
# for i in range(0,10,2): # 0,1,2,3,4,5,6,7,9
#     print('수행문입니다.')
    

# for문을 사용해서 1-100 사이의 홀수를 출력해보세요

# 1) if 사용하지 않음 (증감이용)
# for i in range(1,101,2):
#     print(i, end = ' ')
# 2) if 사용
# for i in range(100):
#     if i%2 != 0: 
#         print(i, end = ' ')

# # 50 - 1 사이의 6의 배수를 역순으로 출력해보세요
# for i in range(48,1,-6):
#     print(i, end = ' ')
    
# input()사용
# 입력 : 두개의 숫자를 입력받음
# 출력 : 사칙연산
        # a + b = c
        # a - b = d
        # a * b = e
        # a / b = f
# 계산을 10번 반복하는 코드를 만드세요 (입력도 10번 반복됨)

for i in range(10):
    a = int(input('첫번째 숫자입력 >> '))
    b = int(input('두번째 숫자입력 >> '))
    c = str(input('연산자 입력(+,-,*,/)'))
    if c == '+':
        print('{} {} {} = {}'.format(a,c,b,a+b))
    elif c == '-':
        print('{} {} {} = {}'.format(a,c,b,a-b))
    elif c == '*':
        print('{} {} {} = {}'.format(a,c,b,a*b))
    elif c == '/':
        print('{} {} {} = {:.2f}'.format(a,c,b,a/b))
    else:
        print('오기입')