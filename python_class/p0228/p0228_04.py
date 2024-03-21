
# 1 - 100 까지의 합
""" 
t1 = 0
for i in range(101):
    t1 += i
print(t1, end=' ') 
 """

# 1 - 100 까지 짝수의 합, 홀수의 합 if절을 사용
""" 
t1 = 0
t2 = 0
for i in range(101):
    if i%2 == 0:
        t1 += i
    else:
        t2 += i
print(t1)
print(t2) 
"""

# 1. 1-10 합

t1 = 0
for i in range(11):
    t1 += i
print(t1) 

# 2. 
num = [1,2,3,4,5,6,7,8,9,10]
t2 = 0
for i in range(len(num)):
    t2 += num[i]
print(t2) 
