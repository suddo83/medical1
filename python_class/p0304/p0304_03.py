#2명의 학생의 국어,영어,수학을 입력받아
#합계를 출력하시오.

students = []
# kor = int(input('국어점수를 입력하세요 >> '))
for i in range(0,2):
    student = [] # 초기화
    student.append(input('이름을 입력하시오 >>'))
    student.append(int(input('국어점수를 입력하시오 >> ')))
    student.append(int(input('수학점수를 입력하시오 >> ')))
    student.append(int(input('영어점수를 입력하시오 >> ')))
    sum = student[1]+student[2]+student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)
    
# 전체학생출력
print("[ 학생성적 출력 ]")
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
# 2차원 리스트는 for문을 2번 사용
# 3명의 국어점수 합계,평균을 출력하시오
for stu in students:
    for s in stu:
       print(s,end='\t')
    print()
print('-'*50)

# students = [['홍길동',100,100,100],['유관순',100,100,100],['이순신',100,100,100]]
# 총 학생의 총 국어점수, 영어점수, 수학점수, 합계, 평균 
kors = 0
engs = 0
maths = 0
totals = 0
avgs = 0

# for i,stu in enumerate(students): # for문
#     kors += stu[1]
#     engs += stu[2]
#     maths += stu[3]
#     totals += stu[4]
i = 0 
while i < len(students): # while 문
    stu = students[i]
    kors += stu[1]
    engs += stu[2]
    maths += stu[3]
    totals += stu[4]
    i += 1

avgs = totals/len(students)
print('\t')
print(kors,engs,maths,totals,avgs,sep='\t')
    
    
    

