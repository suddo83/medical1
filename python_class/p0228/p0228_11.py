# """
# 주석 여러줄 쓸때
# 한줄 주석 # 주석 쓰셔도되고
# control + /  : 커서 있는 문장주석
# tab : 들여쓰기
# shift + tab (들여쓰기 삭제)
# alt + shift + 위아래 방향키 (커서있는 문장 복사) 
# """
# # num = [100,200,300,400]
# # # for문을 사용해서 하나씩 출력해보세요 2가지 방법 다 쓰기

# # for i in num:
# #     print(i, end=' ')

# # for i in range(len(num)):
# #     print(num[i], end='\t')
    
# # numlist = [[1,2],[3,4],[5,6]]
# # for n in numlist:
# #     for a in n:
# #         print(a, end=' ')
# #     print()
# # # in range
# # for i in range(len(numlist)): # for i in range(3)
# #     print(i)
# #     for j in range(len(numlist[i])):
# #         print(numlist[i][j], end=' ')
# #     print()

# f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]
# # 요소 한개한개를 출력해보세요
# for i in range(len(f)):
#     for k in range(len(f[i])):
#         print(f[i][k],end=' ')
#     print()
# # 과일 이름만출력
# print(f[0][0],f[1][0],f[2][0],f[3][0])
# for i in range(len(f)):
#     print(f[i][0])

# for i in range(len(f)):
#     for j in range(len(f[i])):
#         print(f[i][j], end=' ')
#     print()

score = [90,80,70,100,95,85,100]
total = []
# 점수의 총합을 구하세요
# 그 점수를 total리스트에 넣어주세요
sum = 0
for i in score:
    sum += i
print(sum)

sum1 = 0
for i in range(len(score)):
    sum1 += score[i]
    print(i)
    print(score)
    
print(total)
    