# print("a는 %s입니다"%"입력값")
# a = "입력값"
# print("a는 %s입니다"%a)

# 입력함수 : input()
# a = input("값을 입력해주세요 >> ")
# print("a는 %s입니다"%a)

n1 = input("첫번째 숫자를 입력하세요 >> ")
n2 = input("두번째 숫자를 입력하세요 >> ")
# 문자열로 인식이 되어있다
print("두 수의 합 : ", n1+n2)
# 문자를 숫자(정수)로 바꿔준다
# print("두 수의 합 (int 형) : ", int(n1)+int(n2))
# 문자를 숫자(실수)로 바꿔준다
print("두 수의 합 (float 형) : ", float(n1)+float(n2))

a = 10
b = "10"
c = 20
d = "20"
print("숫자일때 :", a+c)
print("문자일때 :", b+d)