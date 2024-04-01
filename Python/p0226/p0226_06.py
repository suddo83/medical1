student = []
 
 # 두명 이상의 학생의
 # 이름, 국, 영, 수 점수를 입력받아 input()사용
 # 리스트를 생성 후,
 # student 리스트에 넣어주세요
 # student 리스트 전체 출력
n1 = input('첫번째 학생의 이름을 입력하시오 >> ')
k1 = int(input('국어성적을 입력하시오 >> '))
e1 = int(input('영어성적을 입력하시오 >> '))
m1 = int(input('수학성적을 입력하시오 >> '))
n2 = input('두번째 학생의 이름을 입력하시오 >> ')
k2 = int(input('국어성적을 입력하시오 >> '))
e2 = int(input('영어성적을 입력하시오 >> '))
m2 = int(input('수학성적을 입력하시오 >> '))

stu1 = [n1,k1,e1,m1]
stu2 = [n1,k1,e1,m2]
student = [stu1,stu2]
print(student)
