#돈을 입력받아
# 5만원권
# 만원권
# 오천원권
# 천원권으로
# 교환해서 출력

money = int(input('교환할돈을 입력하세요 >> '))
c50k, c10k, c5k, c1k = 0,0,0,0

c50k = money//50000
c10k = (money%50000)//10000
c5k = ((money%50000)%10000)//5000
c1k = (((money%50000)%10000)%5000)//1000

print("입력한 금액 : {}".format(money))
print("5만원 : {}".format(c50k))
print("1만원 : {}".format(c10k))
print("오천원 : {}".format(c5k))
print("천원 : {}".format(c1k))