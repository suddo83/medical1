# student클래스 생성, 파일불러와서 클래스에 저장후 출력하시오.
class Student:
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        self.rank = rank
            
    def __str__(self):
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'

    def stu_main_print():
        print('-'*40)
        print('\t[학생성적프로그램]')
        print('-'*40)
        print('1. 학생성적입력')
        print('2. 학생성적전체출력')
        print('3. 학생검색')
        print('4. 학생수정')
        print('5. 등수처리')
        print('6. 학생삭제')
        print('7. 학생성적 파일저장')
        print('0. 프로그램 종료')
        print('-'*40)
        choice = input('원하는 번호를 입력하세요:  ')
        print('-'*40)
        if not choice.isdigit():
            print('숫자만 입력 가능합니다.')
        choice = int(choice)
    
    # stu_main_print()
        
students = []
f = open('stu.txt','r',encoding='utf8')
while True:
    txt = f.readline()
    if txt == '':break
    txt_list = txt.split(',')
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()
#------------------------------------------------
def stu_main_print():
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
#------------------------------------------------

Student.count = len(students)+1
# for stu in students:
#     print(stu)
while True:
    print('-'*40)
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('0. 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요.>> ')
    choice = int(choice)
    if choice == 1:
        while True:
            name = input(f'{len(students)+1}번째 학생이름을 입력하시오.(0.취소)>> ')
            if name == '0':
                print('학생 입력을 취소합니다.')
                break
            kor = int(input('국어점수를 입력하시오.>> '))
            eng = int(input('영어점수를 입력하시오.>> '))
            math = int(input('수학점수를 입력하시오.>> '))
            # list에 추가
            s = Student(name,kor,eng,math)
            students.append(s)
            print('입력데이터 :',s)
    
    elif choice == 2:

        # 데이터 출력
        for i in students:
            print(i) # 객체를 출력
            
        print()
    
    elif choice == 3:
        print('[ 학생성적 검색 ]')
        search = input('찾고자 하는 학생 이름을 입력하세요.>> ')
        
        # 전체리스트에서 학생검색
        s_cnt = 0
        for i in students:
            if search == i.name:
                break
            s_cnt += 1
            
        if s_cnt == len(students):
            stu_main_print()    
            students[s_cnt]
            
        else:
            print('찾고자 하는 학생이 없습니다.다시 검색하세요.')