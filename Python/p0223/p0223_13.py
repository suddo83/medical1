
# # 빈 리스트 생성
# # cont = []

# c1 = input("1.나라를 입력해주세요 >> ")
# c2 = input("2.나라를 입력해주세요 >> ")
# c3 = input("3.나라를 입력해주세요 >> ")
# c4 = input("4.나라를 입력해주세요 >> ")

# # [미국, 영국, 일본, 중국]
# # cont = [c1,c2,c3,c4]    # 출력방법1
# # cont.append(변수)       # 출력방법2 
# cont.append(c1)        
# cont.append(c2)
# cont.append(c3)
# cont.append(c4)
# print(cont)

# # 미국 - 영국 - 프랑스 - 이탈리아
# print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3]))
# print('{}-{}-{}-{}'.format(cont[-4],cont[-3],cont[-2],cont[-1]))

f = [] # 과일리스트
# 내가입력한 과일들로 리스트를 채워보세요 
# 과일3개이상

c1 = input("1.과일을 입력해주세요 >> ")
c2 = input("1.과일을 입력해주세요 >> ")
c3 = input("1.과일을 입력해주세요 >> ")

f=(c1,c2,c3)
print(f[0],f[1],f[2])
print(f[-3],f[-2],f[-1])
# 내가 좋아하는 과일은 딸기, 바나나, 체리 입니다
print('내가 좋아하는 과일은 {},{},{} 입니다'.format(f[-3],f[-2],f[-1]))

