# 동전 교환 프로그램
# money = int(input('교환할돈을 입력하세요 >> '))


money = 1270
c500, c100, c50, c10 = 0,0,0,0
# 1270 > 500백원이 몇개 필요한가?
# 몫: 500원값 나머지값이 다음계산을 위해서 필요한 값

c500 = money//500 # 몫 c500 = 2
# 500원 동전갯수 2 * 500 = 1000 나머지는 270
c100 = (money%500)//100
# 100원 동전갯수
c50 = ((money%500)%100)//50
# 50원 동전갯수
c10 = (((money%500)%100)%50)//10
# 10원 동전갯수

print("입력한 금액 : {}".format(money))
print("500원 : {}".format(c500))
print("100원 : {}".format(c100))
print("50원 : {}".format(c50))
print("10원 : {}".format(c10))


