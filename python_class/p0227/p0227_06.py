# 입력 : 이름 , 아이디 , 비밀번호 (input)
# 5명을 입력받아서 member리스트를 만드세요

member = [] # [[홍길동,aaaa,1111,[유관순,bbbb,2222]]
""" 
member리스트를
이름   아이디   비밀번호
홍길동  aaaa     1111
유관순  bbbb     2222
형식으로 출력해보세요
"""

for i in range(2):
    n1 = input("이름을 입력하시오 >> ")
    id1 = input("아이디를 입력하시오 >> ")
    pass1 = input("비밀번호를 입력하시오 >> ")
    member.append([n1,id1,pass1])
print('이름\t아이디\t비밀번호')
for i in range(len(member)):
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))
        