# 문자열을 사용하여 프린트로 출력하기
str1 = "name"
print("이름을 영어로 하면 무엇일까요?", str1)

# 프린트 시 문자열을 중간에 삽입하는 방법
str2 = "jane"
print('나의 이름은 %s입니다'%str2)
print('나의 이름은 '+str2+'입니다')
print('나의 이름은 {}입니다'.format(str2))

# 정수형 입력
num1 = 10
num2 = 100
print(num1, num2)
print(num1+num2)

# 정수 계산시 print내 사칙연산이 가능하다.
num1 = 20
num2 = 200
num3 = 2000
print("%d+%d+%d=%d"%(num1,num2,num3,num1+num2+num3))

# 실수타입이 있을 때 
num4 = 10
num5 = 100.3
num6 = 1000
print("%d+%f+%d=%f"%(num4,num5,num6,num4+num5+num6))
print("%d+%.1f+%d=%.1f"%(num4,num5,num6,num4+num5+num6))

print("{}+{}+{}={}".format(num4,num5,num6,num4+num5+num6))

# 해보세요
print(200+100)
print(200-100)      
print(200*100)
print(200/100)

# 변수를 사용
a = 100
b = 10
print(a+b)
print(a-b)      
print(a*b)
print(a/b)

print('*'*20)
# 함수를 사용하여 사칙연산 계산

def cal(a,b):
    print(a+b)
    print(a-b)      
    print(a*b)
    print(a/b)
    
cal(100,5)
print('-'*20)
cal(50,2)

num1 = 10
num2 = 5
print(str(num1)+'+'+str(num2)+'='+str(num1+num2))
print(num1,'+', num2,'=',num1+num2)
print('%d+%d=%d'%(num1,num2,num1+num2))
print('{}+{}={}'.format(num1,num2,num1+num2))

# 수식을 10 - 5 = 5 로 출력하기. 4가지 방법을 다 사용해보기
print(str(num1)+'-'+str(num2)+'='+str(num1+num2))
print(num1,'-', num2,'=',num1+num2)
print('%d-%d=%d'%(num1,num2,num1-num2))
print('{}-{}={}'.format(num1,num2,num1-num2))


