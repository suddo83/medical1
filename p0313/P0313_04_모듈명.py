# # import math -> 사용방법 math.floor() 이름.함수명()
from math import * # 이름 생략가능
import lotto45
from lotto45 import *


l = [0]*45
# while True:
# lotto.screen()
screen()
num_generate(l)


# ceil - 올림
print(ceil(12.2)) # 13
# floor - 버림
print(floor(12.9)) # 12
# round - 반올림
print(round(12.6)) # 13
