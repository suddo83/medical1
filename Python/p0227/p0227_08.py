# 반복문
# for i in range(3):
#     print('안녕')
    
# for i in range(3): # i = 0, 1, 2
#     print('안녕')

# 1. 숫자하나를 입력받아서 1부터 입력한 수 까지의 합을 구하세요

sum = 0
n1 = int(input("숫자입력 >> "))
for i in range(1,n1+1,1):
    sum += i
print(sum)

# 2. 1부터 100까지 짝수의 합

sum = 0
n = 100
for i in range(1,n+1,1):    
    if i%2 == 0:
        sum += i
print(sum)


# 3. 1 - 10까지의 곱

sum = 1
for i in range(1,11):    
    sum *=i
print(sum)
