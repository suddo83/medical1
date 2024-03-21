# 함수선언
def cal(num1,num2):
    sum = 0
    if num1 > num2:
        num1,num2 = num2,num1 # 2개변수 치환(only python)
        # temp = num1             # 2개변수 치환(other language)
        # num1 = num2
        # num2 = temp
    for i in range(num1,num2+1):
        sum += i
    return sum
        

# ex) 1,10 -> 
# 두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하시오.
sum = 0
num1 = int(input('1번째 숫자를 입력하세요.>> '))
num2 = int(input('2번째 숫자를 입력하세요.>> '))

sum = cal(num1,num2)

print('합계 : ',sum)