# 1 - 100 까지 더하는데,
# 총 합이 100이 넘었을때 수를 출력하세요

i = 0
sum = 0
while i < 150:
    i += 1
    sum += i
    if sum > 100:
        break
print(sum, i)