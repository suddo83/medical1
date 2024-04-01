num = []
# for문을 사용해서 1-10까지 숫자를 채우세요
for i in range(1,11,1):
    num.append(i)
print(num)

num2 = []
# 1-10까지 짝수를 num2리스트에 넣으세요
for i in range(1,11,2):
    num2.append(i+1)
print(num2, end=' ')

# num = [1,2,3,4,5,6,7,8,9,10]

# num리스트 내의 숫자들의 합을 구하세요
sum = 0
for i in range(len(num)):
    sum += num[i]
print(sum)

# num2리스트 내 숫자들의 합을 구하세요
sum1 = 0
for i in range(len(num2)):
    sum1 += num2[i]
print(sum1)