# 해보세요
cal = input('수식을 입력하세요 (+,-,*,/) >> ')
n1 = int(input('첫번째 숫자 >> '))
n2 = int(input('두번째 숫자 >> '))

if cal == "+":
    # print("{}+{}={}".format(n1,n2,n1+n2)) # 과정과 결과값이 모두 출력
    print(n1+n2)                            # 결과값만 출력
elif cal == "-":
    print("{}-{}={}".format(n1,n2,n1-n2))
elif cal == "*":
    print("{}*{}={}".format(n1,n2,n1*n2))
elif cal == "/":
    print("{}/{}={}".format(n1,n2,n1/n2))
else:
    print('잘못입력하셨습니다')