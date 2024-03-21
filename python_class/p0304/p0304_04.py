students = [['홍길동',90,100,99,299,99.97],['유관순',80,100,99,299,99.97],['이순신',100,100,99,299,99.97]]

# kors = 0
# for i,stu in enumerate(students):
#     kors += stu[1]
    
# print(kors)

kors = 0
i = 0
while i < len(students):
    kors += students[i][1]
    i += 1
print(kors)
