
num = [[10,20],[30,40],[50,60]]

for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j],end = " ")
print()
i = 0
while i < len(num):
    j = 0
    while j < len(num[i]):
        print(num[i][j],end = " ")
        j += 1
    i += 1
