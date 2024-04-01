list = []*10
for i in range(10):
    list[i] += i
print(list)

#2차원 리스트 - 크기가 지정이 안됨.

a_list = [] # 리스트 append 추가를 하게 되면 속도가 느림.
a_list.append(0)
a_list.append(1)
a_list.append(2)
a_list[0] = 3 # 리스트에 값을 넣는것이 속도면으로는 빠름
print(a_list)