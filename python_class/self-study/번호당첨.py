from random import *
# 랜덤한 숫자를 만들어서
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨. 
# 아니면 다시 입력해주세요
# 를 출력하는 프로그램을 만들어보세요
# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))
# print(randint(1,100))

# 입력한 숫자가 랜덤숫자보다 작으면 작습니다 더 큰수를 입력해주세요
# 1. 현재 입력한 숫자 모두를 inputList에 넣으세요
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요
# 3. 10회 도전이 실패한 사람에게 랜덤숫자 알려주기

# i = 0
# while i < 10:
inputList = []
a1 = randint(1,100)
for i in range(10):
    i += 1
    b1 = int(input('숫자입력 >> '))
    inputList.append(b1)
    if a1 == b1:
        print('당첨')
        print(f'당첨된 번호 : {a1}')
        break
    elif a1 > b1:
        print('더 큰수를 입력해주세요')
    elif a1 < b1:
        print('더 작은수를 입력해주세요')
print(inputList)
print(f'당첨된 번호 : {a1}')