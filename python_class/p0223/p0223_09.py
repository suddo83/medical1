import datetime
now = datetime.datetime.now() # 현재를 가져옴
print(now)
# 2024-02-23 13:04:04.470886
month = now.month # 현재 월
# 현재가 봄 여름 가을 겨울
# 12,1,2 겨울. 3,4,5 봄. 6,7,8 여름. 9,10,11 가을
# elif를 사용하세요

if month == 12 or month == 1 or month == 2:
    print("겨울.")
elif month == 3 or month == 4 or month == 5:
    print("봄.")
elif month == 6 or month == 7 or month == 8:
    print("여름.")
else:
    print("가을.")