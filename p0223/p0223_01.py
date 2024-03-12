# 정수
print("{0:d}".format(123))
print("{0}".format(123))
print("{}".format(123))
# 실수
print("{0:f}".format(123))
print("{0}".format(123))
print("{}".format(123))
print("{0:.1f}".format(123))
# 문자
print("{0}".format(123))
print("{}".format(123))

print("{0} {1} {2}".format("빨","주","노"))
print("{0} {2} {1}".format("빨","주","노"))

# 변수
number = 10         # 정수 - int
pi = 3.14           # 실수 - float
result = True       # bool - True, False      
str1 = '문장입니다'  # string
ch = 'A'            # 문자

print(result)

s1 = '1+1=2'
print(s1)
s2 = '{}+{}={}'.format(1,1,2)
print(s2)

# 입력 받기 input()
name = input("이름을 입력하세요")
print("당신의 이름은 {}입니다".format(name))
# input()의 결과 값은 문자형
age = int(input("나이를 입력하세요"))
print('당신은 내년에 {}살입니다.'.format(age+1))

