# 리스트에 숫자 넣을때 한줄로 표현하기
aa = []
for i in range(1,11):
    aa.append(i)

print(aa)

names = ['홍길동','유관순','이순신','강감찬','김구']
# 출력
# 1.홍길동 2.유관순 3.이순신 4.강감찬 5.김구

for i in range(len(names)):
    print('{}.{}'.format(i+1,names[i], end=' '))

# 변수1개 더필요
i = 0
for name in names:
    i += 1
    print('{}.{}'.format(i,names))
    
# enumerate 함수
# index를 넣고 싶을때 사용
for i ,name in enumerate(names):
    print('{}.{}'.format(i,names))

for i ,name in enumerate(names, start=1):
    print('{}.{}'.format(i,names))