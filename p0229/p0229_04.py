# while문과 if문을 사용
# 숫자 두개를 입력받고,
# 연산자를 입력받아서 (+-*/)
# 무한히 계산하는 계산기를 만드는데
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요

while True:
    a1 = int(input('첫번째 숫자입력 >> '))
    if a1 == 0:
        print('프로그램이 종료되었습니다.')
        break
    b1 = int(input('두번째 숫자입력 >> '))
    c1 = str(input('연산자 입력(+,-,*,/)'))
    
    if c1 == '+':
        print('{} {} {} = {}'.format(a1,c1,b1,a1+b1))
    elif c1 == '-':
        print('{} {} {} = {}'.format(a1,c1,b1,a1-b1))
    elif c1 == '*':
        print('{} {} {} = {}'.format(a1,c1,b1,a1*b1))
    elif c1 == '/':
        print('{} {} {} = {:.2f}'.format(a1,c1,b1,a1/b1))
    else:
        print('오기입')
        