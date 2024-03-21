import datetime # 날짜 관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴
y = now.year
m = now.month
d = now.day
h = now.hour
m1 = now.minute
s = now.second
print(type(m)) # type을 알아보는 방법: <class 'int'>

# 시간을 사용해서 지금이 오전이면 오전입니다. 오후면 오후입니다 출력
# 현재는 17시로 오후입니다.
# if h <= 12:
#     print("오전")
# else:
#     print("오후")  
# print("현재는 {}시로 오후입니다.".format(h))

# 짝수달입니다. 홀수달 입니다.

# if m%2 == 0:
#     print("짝수달")
# else:
#     print("홀수달")

# 월 겨울 3-11월이면 겨울이 아닙니다. 그 외의 경우에는 겨울입니다.
# 겨울입니다. 겨울이 아닙니다.

# if 3 < m < 11:
#     print("노윈터")
# else:
#     print("윈터")

