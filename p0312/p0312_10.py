import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K 13장
# 카드 총수 : 52장

def card_creat(list_num,list_shape,list_card):
    for i in range(14):
        list_num[i-1] += i
    list_num[0] = 'A'
    list_num[10] = 'J'
    list_num[11] = 'Q'
    list_num[12] = 'K'
    cnt = 0
    for i in list_shape:
        for j in list_num:
            list_card[cnt] = [i,j]
            cnt += 1
    print(list_card)
    print('카드 갯수: ',len(list_card))

def card_shuffle(list_card):
    random.shuffle(list_card)
    print(list_card)

def card_share(list_card, num_players=3, num_cards=3):
    pass

def card_print(list_card):
    pass
#-----------------------------------------------------------------------------------------------------
list_num = [0]*13
list_shape = ['SPADE','DIAMOND','HEART','CLOVER']
list_card = [[0,0]]*52
while True:
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드5장 나눠주기')
    print('4. 카드5장 확인하기')
    print('-'*40)
    choice = int(input('원하는 번호를 입력하세요.>> '))

    if choice == 1:
        card_creat(list_num,list_shape,list_card)

    elif choice == 2:
        card_shuffle(list_card)

    elif choice == 3:
        card_share(list_card)

    elif choice == 4:
        card_print(list_card)
    else:
        print('프로그램을 종료합니다.')
        break