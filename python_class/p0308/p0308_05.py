card_list = [['spade', 2], ['diamond', 5], ['heart', 8], 
 ['diamond', 'A'], ['spade', 10], ['diamond', 'K'], 
 ['clover', 4], ['spade', 5], ['heart', 'Q'], 
 ['diamond', 2], ['diamond', 4], ['heart', 7], 
 ['clover', 'A'], ['diamond', 7], ['heart', 'A'],
 ['spade', 6], ['diamond', 6], ['clover', 8], 
 ['spade', 8], ['heart', 'J'], ['diamond', 'J'], 
 ['diamond', 'Q'], ['clover', 7], ['spade', 9], 
 ['spade', 3], ['heart', 4], ['clover',10], ['clover', 5], 
 ['spade', 7], ['spade', 'J'], ['spade', 'A'], ['heart', 6], 
 ['diamond', 8], ['heart', 2], ['heart', 5], ['diamond', 9], 
 ['diamond', 3], ['heart',3], ['clover', 9], ['clover', 'Q'], 
 ['clover', 2], ['heart', 'K'], ['diamond', 10], ['spade', 'K'], 
 ['spade', 'Q'], ['clover', 3], ['spade', 4], ['heart', 9], 
 ['clover', 'K'], ['clover', 6], ['heart', 10], ['clover', 'J']]

import random
card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
# 카드 1세트를 구현 : 52장
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # "spade","diamond","heart","clover"
    for j in range(13):
       card_list[cnt] = {'shape':i,'num':num_list[j]}
       cnt += 1
# print(card_list)
random.shuffle(card_list)

print('1. 카드1장 뽑기')
print('2. 카드5장 뽑기')
print('0. 종료')








#
card_list = [  
    {},{}         
]