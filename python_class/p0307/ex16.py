import random

# 리스트 초기화
aList = [0] * 100
for i in range(10):
    aList[i] = 1

print("Original List:", aList)

# 리스트 랜덤하게 섞기
random.shuffle(aList)
print("Shuffled List:", aList)

print("-" * 30)

# 1차원 리스트를 10x10 2차원 리스트로 변환
bLists = [aList[i:i+10] for i in range(0, len(aList), 10)]

# 변환된 2차원 리스트 출력
for row in bLists:
    print(row)
