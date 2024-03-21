students = [{'stuNo':1,'stuName':'홍길동','kor':100}]
students[0]['eng'] = 100   # 리스트내의 딕셔너리의 추가
students[0]['kor'] = 50    # 리스트내의 딕셔너리의 수정
del students[0]['stuName'] # 리스트내의 딕셔너리의 삭제

# print(students)

# 타입 list, dic, int, float, str

for key in students[0]:   
    print(key)            # for 문을 이용한 딕셔너리의 키값 추출
print(students[0].keys()) # 리스트내의 딕셔너리의 키값 추출

for key in students[0]:
    print(students[0][key]) # for 문을 이용한 딕셔너리의 키값 추출
print(students[0].values()) # 리스트내의 딕셔너리의 키값 추출

# 리스트내의 딕셔너리의 (키, 값) 쌍들 추출
print(students[0].items()) 



students = [{'stuNo':1,'stuName':'홍길동','kor':100}]
students[0]['eng'] = 100   # 리스트내의 딕셔너리의 추가
students[0]['kor'] = 50    # 리스트내의 딕셔너리의 수정
del students[0]['stuName'] # 리스트내의 딕셔너리의 삭제

# print(students)

# 타입 list, dic, int, float, str

for key in students[0]:   
    print(key)            # for 문을 이용한 딕셔너리의 키값 추출
print(students[0].keys()) # 리스트내의 딕셔너리의 키값 추출

for key in students[0]:
    print(students[0][key]) # for 문을 이용한 딕셔너리의 키값 추출
print(students[0].values()) # 리스트내의 딕셔너리의 키값 추출

# 리스트내의 딕셔너리의 (키, 값) 쌍들 추출
print(students[0].items()) 



