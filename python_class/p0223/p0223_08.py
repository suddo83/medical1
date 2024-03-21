# 점수를 입력받아서
# 90점이상이면 A 80점이상이면 B
# 70점이상이면 C 나머지는 F를 출력해보세요(elif)

# cal = int(input('점수를 입력하세요 >> '))
# if cal >= 90:
#     print("A")                            
# elif cal >= 80:
#     print("B")
# elif cal >= 70:
#     print("C")
# else:
#     print('F')

# 98점이상 A+ 90-93사이는 A-
# B+, B-, C+, C- (중첩 if)

cal = int(input('점수를 입력하세요 >> '))
if cal >= 98:
    print("A+")
    if 98 <= cal:
        print("A+")                         
    elif 94 <= cal < 98:
        print("A")
else: 
        print("A-")
