# medical_1.csv 파일을 읽어와서 출력하시오.

# 파일열기
f = open('medical_1.csv','r',encoding='utf8')

# 파일읽기
cnt = 0
sum = 0
while True:
    txt = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if txt == '': break
    # print(txt,end="")
    list1 = txt.split(',')
    # print(list1)  
    list1[1] = int(list1[1])
    sum += list1[1]
    print(list1,len(list1))
print('기초생활수급대상자 전체 수 : ',sum)
# 파일닫기
# medical_1.csv 파일을 읽어와서 출력하시오.

# 파일열기
f = open('medical_1.csv','r',encoding='utf8')

# 파일읽기
cnt = 0
sum = 0
while True:
    txt = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if txt == '': break
    # print(txt,end="")
    list1 = txt.split(',')
    # print(list1)  
    list1[1] = int(list1[1])
    sum += list1[1]
    print(list1,len(list1))
print('기초생활수급대상자 전체 수 : ',sum)
# 파일닫기
f.close()