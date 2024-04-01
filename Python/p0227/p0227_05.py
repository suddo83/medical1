
# 0 - 20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# 출력 : [0,5,10,15,20]
num=[]
for i in range(0,21,5):
    print(i)
    num.append(i)
print(num)

lan = ['c','python','java','jquery','css']

# 1. 하나하나 출력해보기
for i in lan:
    print(i)
for i in range(len(lan)):
    print(lan[i])
# 2. 1. c
#    2. python
#    3. java
#    4. jquery
#    5. css
#    이렇게 출력해보기
for i in range(5):
    print('{}. {}'.format(i+1,lan[i]))

num = [1,-1,2,3,-4,5,6,-8,9,-10]
for i in num:
    if i > 0:
        print("{}   : 양수".format(i))
    else:
        print("{}  : 음수".format(i))

for i in range(len(num)):
    if num[i] > 0:
        print("{}   : 양수".format(i))
    else:
        print("{}  : 음수".format(i))

# 양수면 양수 음수면 음수 출력 for사용
# 1: 양수
# -1: 음수
# 2: 양수..
        