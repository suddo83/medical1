# if 문을 사용해서 1누르면 [학생성적입력]
# 4 누르면 [학생성적전체출력]
# 0 누르면 [프로그램 종료]
stu=[]

for i in range(5): # for 를 사용해서 5번 반복
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')      
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = int(input('원하는 번호를 입력하세요 >> '))
    if ch == 1:
        print('[학생성적입력]') 
        n1 = input('학생의 이름을 입력하시오 >> ') # 이름, 국어, 영어, 수학 점수를 입력받아
        k1 = int(input('국어성적을 입력하시오 >> '))
        e1 = int(input('영어성적을 입력하시오 >> '))
        m1 = int(input('수학성적을 입력하시오 >> '))
        stu.append([1,n1,k1,e1,m1,k1+e1+m1,(k1+e1+m1)/3,1])
    elif ch == 4:
        print('[학생성적전체출력]') 
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for i in range(len(stu)): # 출력 for를 사용해서 학생 수만큼 출력
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
            .format(stu[i][0],stu[i][1],stu[i][2],stu[i][3]
              ,stu[i][4],stu[i][5],int(stu[i][6]),stu[i][7]))
    elif ch == 0:
        print('[프로그램 종료]')
    else:
        print('잘못 입력하셧습니다')
 
