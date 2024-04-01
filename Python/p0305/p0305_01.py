# 리스트에 1,25까지 숫자를 리스트에 입력하시오.
list_a =[]

# i = 0
# while i <= 25:
#     list_a.append(i)
#     i += 1
# print(list_a)


# 1부터 25까지 2차원 리스트 생성
# 빈 리스트 생성
i = 1
while i <= 25:
    temp_list = []
    j = i
    while j < i + 5:
        temp_list.append(j)
        j += 1
    list_a.append(temp_list)
    i += 5

# 결과 출력
for k in list_a:
    print(k)
print(list_a)