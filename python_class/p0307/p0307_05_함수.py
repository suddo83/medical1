words = [ {},
    { 
    'airplane':'비행기','apple':'사과','bakery':'빵집',
    'banana':'바나나','bank':'은행','bean':'콩',
    'bicycle':'자전거','boat':'보트','bowl':'그릇','bus':'버스'    
    },{
    "run" : "달리다",
    "walk" : "걷다",
    "sit" : "앉다",
    "stand" : "서다",
    "sleep" : "자다",
    "read" : "읽다",
    "look" : "보다",
    "do" : "하다",
    "feel" : "느끼다",
    "go" : "가다"
    },{
    "accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의",
}]
w_noun = { 
    'airplane':'비행기','apple':'사과','bakery':'빵집',
    'banana':'바나나','bank':'은행','bean':'콩',
    'bicycle':'자전거','boat':'보트','bowl':'그릇','bus':'버스'   
    }
w_verb = {
    "run" : "달리다",
    "walk" : "걷다",
    "sit" : "앉다",
    "stand" : "서다",
    "sleep" : "자다",
    "read" : "읽다",
    "look" : "보다",
    "do" : "하다",
    "feel" : "느끼다",
    "go" : "가다"
    }
w_ad = {
    "accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의",
}
w_title = ['','명사','동사','형용사']

# 함수선언
def w_quiz():
    print("{}를 선택하셧습니다.".format(w_title[choice]))
    chk = input('퀴즈가 나갑니다. 준비되셨나요?(1.실행, 0.취소)')
    if chk == "1":
        # 퀴즈 프로그램
        # key-영문, value-한글
        # print(w_noun.key()) # 전체 key
        # print(w_noun.values()) # 전체 value
        count = 0
        for key in words[choice]:
            # print(key,w_noun[key])
            answer = input('{} 단어의 뜻은?'.format(key))
            if words[choice] == answer:
                print('정답.')
                count += 1
            else:
                print('오답. 정답은 {}입니다.'.format(words[choice][key])) 
        print('총 {}문제를 맞추셧습니다.'.format(count))       
    else:
        print('퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.')


while True:
    print('[ 영단어 맞추기 프로그램]')
    print('-'*40)
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print('-'*40)
    choice = int(input('원하는 번호를 입력하세요.>> ')) # 정수형으로 받음.

    if choice == 1:
        w_quiz()
    elif choice == 2:
        w_quiz()
    elif choice == 3:
        w_quiz()
    else:
        print('프로그램을 종료합니다.')
        break