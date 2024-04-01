# # 1 - 5까지의 합계를 구하세요
# sum = 1+2+3+4+5

# total = 0           # t = 0
# total = total + 1   # t = 1
# total = total + 2   # t = 1 + 2
# total = total + 3   # t = 1 + 2 + 3
# total = total + 4   # t = 1 + 2 + 3 + 4
# total = total + 5   # t = 1 + 2 + 3 + 5
# print(total)

# t = 0
# for i in range(1,6,1): # i = 1,2,3,4,5
#     t = t + i
# t = 0
# for i in range(1,6,1): # i = 1,2,3,4,5
#     t += i
# print(t)

# 1 에서 10까지의 합을 구해보세요 for
# t = 0
# for i in range(1,11,1):
#     t += i
# print(t)

# for i in range(1,101,1):
#     t += i
# print(t)

# 입력한 수부터 입력한 수 까지의 합을 구해보세요
sum = 0
n1 = int(input('숫자1 >> '))
n2 = int(input('숫자2 >> '))
for i in range(n1,n2+1,1):
    sum += i
print(sum)
    
