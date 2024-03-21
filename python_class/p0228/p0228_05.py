n1 = int(input("숫자1 >> "))
n2 = int(input("숫자2 >> "))
sum = 0
# # n1 부터 n2까지의 합
# if n1 > n2:
#     n1,n2 = n2,n1
# for i in range(n1,n2+1):
#     sum += i
# print(sum)

# 3. n1-n2까지의 홀수 값을 저장
odd_list = []
for i in range(n1,n2+1):
    if i%2 != 0:
        odd_list.append(i)
print(odd_list)
