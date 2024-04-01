# stu.txt파일을 출력하시오.
file = open('stu.txt','r',encoding='utf8')
list1=[]
while True:
    txt = file.readline() # 파일 1줄 읽어오기
    if txt == '': break
    list1 = txt.split(',')
    list1[0] = int(list1[0].strip())
    list1[1] = list1[1].strip()
    list1[2] = int(list1[2].strip())
    list1[3] = int(list1[3].strip())
    list1[4] = int(list1[4].strip())
    list1[5] = int(list1[5].strip())
    list1[6] = float(list1[6].strip())
    print(list1)


# # 파일 읽어오기

# file = open('str.txt','r',encoding='utf8')
# while True:
#     txt = file.readline() # 파일 1줄 읽어오기
#     if txt == '':
#         break
#     print(txt,end='')


# file.close()


# # 파일저장
# file = open('str.txt','w',encoding='utf8')

# file.write('안녕하세요. 반갑습니다.\n')
# file.write('저는 홍길동입니다..\n')
# file.write('파이썬 수업을 열심히 듣고 있습니다.\n')

# file.close()
# print('파일이 저장되었습니다.')
# stu.txt파일을 출력하시오.
file = open('stu.txt','r',encoding='utf8')
list1=[]
while True:
    txt = file.readline() # 파일 1줄 읽어오기
    if txt == '': break
    list1 = txt.split(',')
    list1[0] = int(list1[0].strip())
    list1[1] = list1[1].strip()
    list1[2] = int(list1[2].strip())
    list1[3] = int(list1[3].strip())
    list1[4] = int(list1[4].strip())
    list1[5] = int(list1[5].strip())
    list1[6] = float(list1[6].strip())
    print(list1)


# # 파일 읽어오기

# file = open('str.txt','r',encoding='utf8')
# while True:
#     txt = file.readline() # 파일 1줄 읽어오기
#     if txt == '':
#         break
#     print(txt,end='')


# file.close()


# # 파일저장
# file = open('str.txt','w',encoding='utf8')

# file.write('안녕하세요. 반갑습니다.\n')
# file.write('저는 홍길동입니다..\n')
# file.write('파이썬 수업을 열심히 듣고 있습니다.\n')

# file.close()
# print('파일이 저장되었습니다.')
