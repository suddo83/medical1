# n1단부터 n2단 까지 출력하세요
n1 = int(input('숫자1 입력 >> '))
n2 = int(input('숫자2 입력 >> '))

# # 출력 2, 4 2단부터 4단까지 출력
for i in range(n1,n2+1):
    # print('[{}단]'.format(i))
    for k in range(1,10,1):
        print('[{} * {} = {}]'.format(i, k, k*i), end = '\t')
    print()
    
for i in range(1,10,1):
    # print('[{}단]'.format(i))
    for k in range(n1,n2+1):
        print('[{} * {} = {}]'.format(k, i, k*i), end = '\t')
    print()

# 크기비교해서 n1더 크면 n2, n1값 바꾸기