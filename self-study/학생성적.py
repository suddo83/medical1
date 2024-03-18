# 프로그램 작성하시오.
students = [
        {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
        {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
        {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
        {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
        {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
        ]
cnt = len(students)+1 # 학생5명이 입력되어있으므로 카운터 변수를 +1로지정
while True:
    print('-'*50)
    print('[학생성적프로그램]')
    print('-'*50)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생성적수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*50)
    ch = input('번호를 입력하시오.>> ')
    if not ch.isdigit():
        print('숫자만 입력가능')
        continue
    ch = int(ch)

    if ch == 1:
        while True:
            ch1 = input(f'{len(students)+1}번째 학생의 이름을 입력하시오.(0.취소)>> ')
            if ch1 == '0':
                print('학생 입력을 취소합니다.')
                break
            kor = int(input('국어점수를 입력하시오.>> '))
            eng = int(input('영어점수를 입력하시오.>> '))
            math = int(input('수학점수를 입력하시오.>> '))
            total = kor + eng + math
            avg = total/3
            student = {'stuNo': f'S{len(students) + 1:03d}', 'name': ch1, 'kor': kor, 'eng': eng, 'math': math, 'total': total, 'avg': f'{avg:.2f}'}
            students.append(student)
            cnt += 1
            print('입력 학생정보: ',student)
            print('저장된 학생정보: ')
            for i in students:
                print(i)

    elif ch == 2:
        while True:
            ch2 = input('학생성적전체출력을 하시겠습니까?(1.확인 0.취소)>> ')
            if ch2 == '0':
                break
            elif ch2 == '1':
                print("\t[ 학생성적 출력 ]")
                print('-'*65)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
                print('-'*65)
                for student in students:
                    print(f'{student['stuNo']}\t{student['name']}\t{student['kor']}\t{student['eng']}\t{student['math']}\t{student['total']}\t{student['avg']}\t{student['rank']}\t')
                print('-'*65)
            else:
                print('잘못 입력하셨습니다.')
                
    elif ch == 3:
        pass

    elif ch == 4:
        subject = ['','국어','영어','수학']
        while True:
            ch4 = input('찾는 학생의 이름을 입력하시오.(0.취소)>> ')
            chk = 0 
            if ch4 == '0':
                break
            for s_dic in students:
                if s_dic['name'] == ch4:
                    break
                chk += 1
            print('찾은 학생의 위치 :', chk)
            if chk == len(students): 
                print(f'{ch4} 학생은 없습니다. 다시 입력하시오.')
            else:
                print(f'{ch4} 학생을 찾았습니다.')
                while True:
                        print("[ 수정할 과목 선택 ]")
                        print("-"*30)
                        print("1.국어\t2.영어\t3.수학")
                        s_input = int(input('수정하려는 과목을 선택하시오.(0.취소)>> '))
                        if s_input == 0:
                            break
                        elif s_input == 1:
                            s1 = 'kor'
                            print(f'{subject[s_input]} 수정')
                            print(f'현재 {subject[s_input]}점수 : {students[chk][s1]}')
                            print("-"*30)
                            score = int(input(f'수정할 {subject[s_input]}점수를 입력하시오.>> '))
                            students[chk][s1] = score
                            students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                            students[chk]['avg'] = float(f'{students[chk]['total']/3:.2f}')
                            print(f'{subject[s_input]}점수 : {students[chk][s1]}점으로 수정이 완료되었습니다.')
                            print(students[chk])
                        elif s_input == 2:
                            s1 = 'eng'
                            print(f'{subject[s_input]} 수정')
                            print(f'현재 {subject[s_input]}점수 : {students[chk][s1]}')
                            print("-"*30)
                            score = int(input(f'수정할 {subject[s_input]}점수를 입력하시오.>> '))
                            students[chk][s1] = score
                            students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                            students[chk]['avg'] = float(f'{students[chk]['total']/3:.2f}')
                            print(f'{subject[s_input]}점수 : {students[chk][s1]}점으로 수정이 완료되었습니다.')
                            print(students[chk])
                        elif s_input == 3:
                            s1 = 'math'
                            print(f'{subject[s_input]} 수정')
                            print(f'현재 {subject[s_input]}점수 : {students[chk][s1]}')
                            print("-"*30)
                            score = int(input(f'수정할 {subject[s_input]}점수를 입력하시오.>> '))
                            students[chk][s1] = score
                            students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                            students[chk]['avg'] = float(f'{students[chk]['total']/3:.2f}')
                            print(f'{subject[s_input]}점수 : {students[chk][s1]}점으로 수정이 완료되었습니다.')
                            print(students[chk])
                        else:
                            print('잘못 입력하셨습니다.')
                   
    elif ch == 5:
        for s_dic in students:
            rank = 1
            for i_dic in students:
                if s_dic['total'] < i_dic['total']:
                    rank += 1
            s_dic['rank'] = rank
        print('등수처리가 완료되었습니다.')
        # sorted_students = sorted(students, key=lambda x: x['total'], reverse=True) # 등수 내림차순으로 정렬
        for i in students:
            print(i)
        
    elif ch == 6:
        ch6 = input('삭제하려는 학생의 이름을 입력하시오.(0.취소)>> ')
        chk = 0 
        if ch6 == '0':
            break
        for s_dic in students:
            if s_dic['name'] == ch6:
                break
            chk += 1
        print('찾은 학생의 위치 :', chk)
        if chk >= len(students): 
            print(f'{ch6} 학생은 없습니다. 다시 입력하시오.')
        else:
            print(f'{ch6} 학생을 찾았습니다.')
            ch6_1 = input(f'{ch6} 학생 성적을 삭제하시겠습니까?(1.실행 0.취소)')
            if ch6_1 != "1":
                print('삭제가 취소되었습니다.')
                break
            else:
                del students[chk]
                print(f'{ch6} 학생성적이 삭제 되었습니다.')
                print(students)

    elif ch == 0:
        pass        
        print('프로그램 종료')
        break
    else:
        print('선택된 항목이 없습니다')


