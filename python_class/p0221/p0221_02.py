print("hello Python")
print("Hello"*3)
print("혼자 공부하다 모르면 동영상 강의를 참고하세요!")

print(5 > 10) #False
print(5 < 10) #True
print(True)
print(False)

print(not True) #False
print(not (5>10)) #True
# "" '' 안에 있는 것은 문자열이다

print(0*10)      # 숫자 0
print("0"*10)

print("100+100") # 문자
print(100+100)   # 숫자

print("숫자는 %d"%300)
print("%d" % 200)
print("%d+%d=%d"%(2,3,2+3))

print("%d"%123)
print("%7d"%123)        # 7자리 숫자를 보여줌. 빈공백으로 채움. 여백의 갯수
print("%05d"%123)       # 5자리 숫자를 보여줌. 빈공백은 0으로 채움

# %d : 정수
# %f : 실수

print("%d"%123.45)
print("%f"%123.45)

print("%7.1f"%123.45)   # 소숫점을 포함해서 총 7자리 출력
# 빈 공백으로 채움. 소숫점이하는 1자리까지 표현

print("%7.3f"%12.3456)   # 소숫점이하는 3자리로 표현하고 빈공백은 0으로 채움
print("%.2f"%12.3456)

#문자열은 %s를 사용
print("안녕하세요")
print("%s"%"반갑습니다")
# 문자는 %c를 사용
print("%c"%'a')

print("%.2f"%758.12345678)  # 문제1

print("%010.2f"%25.05)      # 문제2

print("%d"%150.15)          # 문제3
print("%f"%150.15)
print("%s"%150.15)

print("*"*10)               # 문제4


