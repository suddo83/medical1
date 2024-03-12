# for 문을 사용해서 2단을 출력
# 입력받은 숫자의 단을 출력하세요 >>
# 3을 입력받으면 3단 출력 4를 입력받으면 4단 출력

# for k in range(9):
#     n = int(input('구구단을 외자 >> '))
#     print('[{}단]'.format(n))
#     for i in range(1,10):
#         print('[{} * {} = {}]'.format(n, i, n*i), end = ' ')
#     print()

# 짝수단만 출력해주세요
for k in range(1,10,1):
    if k%2 == 0:
        print('[{}단]'.format(k))
        for i in range(1,10):
            print('[{} * {} = {}]'.format(k, i, k*i), end = ' ')
        print()
# 홀수단만 출력해보세요
for k in range(1,10,1):
    if k%2 == 1:
        print('[{}단]'.format(k))
        for i in range(1,10):
            print('[{} * {} = {}]'.format(k, i, k*i), end = ' ')
        print()

for k in range(1,10,1):
        print('[{}단]'.format(k))
        for i in range(1,10):
            if i%2 == 1:
                print('[{} * {} = {}]'.format(k, i, k*i), end = '')
        print()
print()    