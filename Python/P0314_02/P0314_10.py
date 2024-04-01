# k001.csv 파일에서 전국 인원수를 출력하시오.
# 적용년월,시도코드,시도명,사용건수,인원수,사용금액
f = open('k001.csv','r',encoding='utf8')


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
    list1[4] = int(list1[4])
    sum += list1[4]
    print(list1,len(list1))
    # print(txt,end='')
print('총 인원 수 : ',sum)

# k001.csv 파일에서 전국 인원수를 출력하시오.
# 적용년월,시도코드,시도명,사용건수,인원수,사용금액
f = open('k001.csv','r',encoding='utf8')


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
    list1[4] = int(list1[4])
    sum += list1[4]
    print(list1,len(list1))
    # print(txt,end='')
print('총 인원 수 : ',sum)

f.close()