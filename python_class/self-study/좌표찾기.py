import random

# 1차원 리스트 생성 및 초기화
list1 = [0] * 25
for i in range(5):
    list1[i] = 1

print("Original list1:", list1)

# 리스트 랜덤하게 섞기
random.shuffle(list1)
# print("Shuffled list1:", list1)

# 1차원 리스트를 5x5 2차원 리스트로 변환
list2 = [list1[i:i+5] for i in range(0, len(list1), 5)]
# print(list2)

# 새로운 2차원 리스트 생성 및 초기화
list2 = [[0] * 5 for _ in range(5)]
# print(list2)

# 1차원 리스트의 요소를 2차원 리스트에 넣기
for i in range(5):
    for j in range(5):
        list2[i][j] = list1[5 * i + j]

# 출력
for i in range(5):
    print(i,end='\t')
    for j in range(5):
        print(list2[i][j],end='\t')
    print()
import random

# 1차원 리스트 생성 및 초기화
list1 = [0] * 25
for i in range(5):
    list1[i] = 1

print("Original list1:", list1)

# 리스트 랜덤하게 섞기
random.shuffle(list1)
# print("Shuffled list1:", list1)

# 1차원 리스트를 5x5 2차원 리스트로 변환
list2 = [list1[i:i+5] for i in range(0, len(list1), 5)]
# print(list2)

# 새로운 2차원 리스트 생성 및 초기화
list2 = [[0] * 5 for _ in range(5)]
# print(list2)

# 1차원 리스트의 요소를 2차원 리스트에 넣기
for i in range(5):
    for j in range(5):
        list2[i][j] = list1[5 * i + j]

# 출력
for i in range(5):
    print(i,end='\t')
    for j in range(5):
        print(list2[i][j],end='\t')
    print()
