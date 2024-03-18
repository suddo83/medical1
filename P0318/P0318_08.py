class Card(): # 4개의 변수 : kind,number,width,height
    width = 100     # 클래스변수
    height = 200    # 클래스변수
    kind = ''
    number = ''
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200
        



# 클래스 5개를 생성해서 kind = 'spade', num = 1,2,3,4,5
# 클래스를 출력하시오.
c1 = Card('spade',1)
print(f'카드 : {c1.kind},{c1.number}')
c2 = Card('spade',2)
print(f'카드 : {c2.kind},{c2.number}')
c3 = Card('spade',3)
print(f'카드 : {c3.kind},{c3.number}')
c4 = Card('spade',4)
print(f'카드 : {c4.kind},{c4.number}')
c5 = Card('spade',5)
print(f'카드 : {c5.kind},{c5.number}')





# # 52장 카드 생성
# shape = ['SPADE','DIAMOND','HEART','CLOVER']
# number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# card_list = []

# for i in range(4):
#     for j in range(13):
#         c = Card(shape[i],number[j]) # 객체선언
#         card_list.append(c)          # 리스트추가

# for i in range(52):
#     c = card_list[i] # c = Card객체
#     print('카드 출력 : ',c.kind, c.number)
    
    
        



