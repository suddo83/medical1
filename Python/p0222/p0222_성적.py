# 학생 이름, 국어, 영어, 수학 점수를 입력받아서
# 아래와 같이 출력을하고

# 만약에 평균이 80점이상이면 합격입니다를 출력하세요

name = input("학생이름을 입력하시오 >> ")
kor = int(input("학생의 국어성적을 입력하시오 >> "))
eng = int(input("학생의 영어성적을 입력하시오 >> "))
math = int(input("학생의 수학성적을 입력하시오 >> "))
avg = int((kor+eng+math)/3)

print('-'*60)
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t {} \t {} \t {} \t {} \t {} \t {} \t'.format(1,name,kor,eng,math,(kor+eng+math),avg,1))
print('-'*60)
if avg >= 80:
    print("홍길동님 합격입니다")
else:
    print("홍길동님 불합격입니다")
    
# print("문자열 {}".format(값))
# 값 = 10
# print(f"값은 {값}입니다.")
# pi = 3.141592653589793
# print("파이의 값은 {:.2f}입니다.".format(pi))


