students=[]
cnt = 0
while True: # 입력>출력>검색>삭제>수정
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')          
    print('4. 학생성적전체출력')
    print('5. 학생검색출력')
    print('6. 등수처리')    
    print('0. 프로그램 종료')
    print('-'*35)
    ch = int(input('원하는 번호를 입력하세요 >> '))
    print('입력하신 번호는 {}입니다'.format(ch))
    if ch == 1:
        print('[학생성적입력]') 
        n1 = input('학생의 이름을 입력하시오 >> ')
        k1 = int(input('국어성적을 입력하시오 >> '))
        e1 = int(input('영어성적을 입력하시오 >> '))
        m1 = int(input('수학성적을 입력하시오 >> '))
        students.append([1,n1,k1,e1,m1,k1+e1+m1,(k1+e1+m1)/3,1])
    elif ch == 4:
        print('[학생성적전체출력]')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for i in range(len(students)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
            .format(students[i][0],students[i][1],students[i][2],students[i][3]
              ,students[i][4],students[i][5],int(students[i][6]),students[i][7]))
    elif ch == 5:
        name1 = input('검색할 학생의 이름을 입력해주세요 >> ')
        print('번호\t이름')
        print('-'*35)
        a1 = 0
        while a1 < len(students):
            if name1 == students[a1][1]:
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
                .format(students[a1][0],students[a1][1],students[a1][2],students[a1][3]
                ,students[a1][4],students[a1][5],int(students[a1][6]),students[a1][7]))
            a1 += 1
    elif ch == 0:
        print('[프로그램 종료]')
        break
    else:
        print('잘못 입력하셧습니다')