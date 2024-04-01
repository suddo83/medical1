# member = []

# # 입력 : 이름, 점수 (input) ['홍길동',90]
# # 총 3명의 정보를 member리스트에 넣으세요
# for i in range(3):
#     name = input('이름입력 >> ')
#     score = int(input('점수입력 >> '))
#     member.append([name,score])
# print(member) # [['홍길동',90],['유관순',91],['이순신',95]]
member = [['홍길동',55],['유관순',80],['이순신',90]]

# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다
# member 변수 사용, for, if


for i in range(len(member)):
    if member[i][1] >= 60: 
        print('{}님 합격입니다'.format(member[i][0]))
    else:
        print('{}님 불합격입니다'.format(member[i][0]))