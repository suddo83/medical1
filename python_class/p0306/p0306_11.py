students = [
        {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
        {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
        {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
        {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
        {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
stu_cnt = len(students)+1
while True:
    print('-'*50)
    print('[학생성적프로그램]')
    print('-'*50)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*50)
    ch = input('원하는 번호를 입력하세요 >> ')
    if not ch.isdigit():
        print('숫자만 입력가능합니다')
        continue
    ch = int(ch)
    
    if ch == 1:
        while True:
            name = input(f'{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)')
            if name == '0':
                print('학생 입력을 취소합니다.')
                break
            student = {}
            students['stuNo'] = 'S'+'{:03d}'.format(stu_cnt)
            students['name'] = name
            kor = int(input('국어점수를 입력하세요.'))
            student['kor'] = kor
            eng = int(input('국어점수를 입력하세요.'))
            student['eng'] = eng
            math = int(input('국어점수를 입력하세요.'))
            student['math'] = math
            total = kor+eng+math
            student['total'] = total
            avg = total/3
            students['avg'] = float('{:.2f}'.format(avg))
            students.append(student)
            stu_cnt += 1
            print('입력 데이터: ',student)
            print(students)
# 학생성적입력 부분 구현하시오.

# 학생성적출력 부분 구현하시오.
    elif ch == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print('선택된 서비스가 없습니다.')