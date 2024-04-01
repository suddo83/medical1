# print('2단 출력')
# for i in range(1,10):
#     print('2 * {} = {}'.format(i, 2*i))
# for i in range(1,10):
#     print('{} * {} = {}'.format(2, i, 2*i))

# 원하는 단을 입력받아서 구구단을 입력하세요
# 3을 입력받으면 3단 출력

for k in range(9):
    n = int(input('구구단을 외자 >> '))
    for i in range(1,10):
        print('{} * {} = {}'.format(n, i, n*i))