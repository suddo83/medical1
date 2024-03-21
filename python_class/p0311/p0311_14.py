def stu_update(student):                                # 지역변수 -> 주소값이 저장
    student['stuNo'] = 2
    student['name'] = '유관순'
    student['total'] = student['kor']+student['eng']+student['math']       # 지역변수
    student['avg'] = student['total'] / 3                         # 지역변수


# 프로그램 구현
student = {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}


# 함수호출
stu_update(student) # 전역변수

print('학번 : ',student) # 1,홍길동,100,100,100,300,100.0
