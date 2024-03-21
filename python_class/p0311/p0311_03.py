
# 구구단 - 이중for문을 사용하고 있음.
# 변수를 1개 사용해야 함.
for i in range(1,10):
    for j in range(1,10):
        if j == 5:
            break
        print(f'{i} * {j} = {i*j}')