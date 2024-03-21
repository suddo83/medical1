list = [
    [0,0,0],[0,0,0],[0,0,0]
]

# 1차원 리스트에 1-9까지의 숫자를 입력하시오.
list = []
for i in range(9):
    list.append(i+1)
print(list)

list2 = [n+1 for n in range(9)]
print(list2)

list3 = [[0]*3 for n in range(3)]

numlist = [num*num for num in range(1,6)]

# 1-9까지의 2차원 리스트에 숫자를 입력하시오.
#[[1,2,3]
# [4,5,6]
# [7,8,9]]

list1 = []
for i in range(3):
    list1 = []
    for j in range(3):
        list1.append(j)  # [0,1,2]
    list1.append(list1) # [[0,1,2],[0,1,2],[0,1,2]]
    
print(list1)
# for i in list:
#     for f in i:
#         print(f,end='\t')
#     print()