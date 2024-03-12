# 입력 : 이름, 점수 (5명의 이름과 점수를 입력받습니다.)
# 60점 이상이면 합격, 60점 미만이면 불합격을출력하는데
# 출력의 형태는 [홍길동님 합격입니다] [홍길동님 불합격입니다]

for i in range(5):
    name = input('이름을 입력하세요 >> ')
    score = int(input('점수를 입력하세요 >> '))
    if score >= 60:
        print('{}님 합격입니다'.format(name))
    else:
        print('{}님 불합격입니다'.format(name))