# 해보세요
# 1. 나이가 10살이상이고 150이상만 탑승가능
# 나이, 키를 입력받아
# [탑승가능] [탑승불가능]을 출력해보세요

age = int(input('나이입력 >> '))
height = int(input('키입력 >> '))

if age >= 10 and height >=150:
    print ('[탑승가능]')
else:
    print ('[탑승불가능]')
    
# 2. 숫자3개 (정수)를 입력받고, 연산1개를 입력받아
# +++ --- *** /// (나누기값은 둘째자리까지 표현)
# a + b + c = d의 형태로 출력   (1 + 2 + 3 = 6)

n1 = int(input('첫번째 숫자입력 >> '))
n2 = int(input('두번째 숫자입력 >> '))
n3 = int(input('세번째 숫자입력 >> '))
n4 = input('사칙연산 선택(+,-,*,/) >> ')
n5 = 0

if n4 == '+':
    n5 = n1+n2+n3
    print('{}+{}+{}={}'.format(n1,n2,n3,n5))
elif n4 == '-':
    n5 = n1-n2-n3
    print('{}-{}-{}={}'.format(n1,n2,n3,n5))
elif n4 == '*':
    n5 = n1*n2*n3
    print('{}*{}*{}={}'.format(n1,n2,n3,n5))
elif n4 == '/':
    n5 = n1/n2/n3
    print('{}/{}/{}={:.2f}'.format(n1,n2,n3,n5))
else:
    print=('잘못입력하셧습니다')
