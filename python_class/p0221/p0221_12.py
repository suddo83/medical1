# 변수명 : stu_no, stu_name, kor, eng, math, total, avg, rank
# 출력 : 
# 번호   이름    국어    영어     수학    합계    평균     등수
#  1    홍길동   100     100     100     300   100.00     1

stu_no = str(1)
stu_name = "홍길동"
kor = int(100)
eng = int(100)
math = int(100)
total = kor+eng+math
avg = total / 3 
rank = str(1)

print("번호\t","이름\t","국어\t","영어\t","수학\t","합계\t","평균\t","등수\t")
print(stu_no + "\t" + stu_name + "\t" + str(kor) + "\t" + str(eng) + "\t" + str(math) + "\t" + str(total) + "\t" + str(avg) + "\t" + rank)

# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list)
# print(total)  # 출력: 15

# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list, 10)  # 초기값을 10으로 지정
# print(total)  # 출력: 25 (10 + 1 + 2 + 3 + 4 + 5)
