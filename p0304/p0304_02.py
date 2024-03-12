# 숫자 6개를 입력받아 출력하시오.
# 1. 숫자 1개 입력
# 2. 숫자 1개 출력

nums = []
sum = 0
for i in range(5):
    nums.append(int(input('숫자입력 >> ')))
    sum += i
print(sum)

sum = 0
for num in nums:
    sum += num
print('합계 :', sum)
