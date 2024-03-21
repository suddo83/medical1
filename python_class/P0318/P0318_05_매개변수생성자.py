class TV:
    channel = 0
    color = 'black'
    size = 65
    volume = 0
    
    def __init__(self,channel=0,color='',size=0,volume=0):
        self.color = color
        self.size = size
        self.volume = volume
        self.channel = channel
        
    def up_volume(self,volume):
        self.volume += volume
    def down_volume(self,volume):
        self.volume -= volume
    
    def up_channel(self,channel):
        self.channel += channel
    def down_channel(self,channel):
        self.channel -= channel
    
    
# 철수-화이트,채널 10변경,2증가
# 영희-핑크,채널 7변경,5증가
# 반장-실버,채널 1변경,3증가

c1 = TV(10,'white',65,0)
# (channel=10,color='white',size=65,volume=0)
c1.up_channel(2)
# c1.channel = 10
# c1.color = 'white'
# c1.size = 65
# c1.volume = 0

c2 = TV(7,'pink',65,0)
# (channel=7,color='pink',size=65,volume=0)
c2.up_channel(5)
# c2.channel = 7
# c2.color = 'pink'
# c2.size = 65
# c2.volume = 0

c3 = TV(1,'silver',65,0)
# (channel=1,color='silver',size=65,volume=0)
c3.up_channel(3)
# c3.channel = 1
# c3.color = 'pink'
# c3.size = 65
# c3.volume = 0

print('철수의 tv : ',c1.channel,c1.color,c1.size,c1.volume)
print('영희의 tv : ',c2.channel,c2.color,c2.size,c2.volume)
print('반장의 tv : ',c3.channel,c3.color,c3.size,c3.volume)
#-----------------------------------------------------------

# class Tv: #클래스선언 - 설계도
#     channel = 0
#     color = "black"
#     size = 65
#     volume = 0
#     def __init__(self,color="",size=0,volume=0,channel=0):
#         self.color = color
#         self.size = size
#         self.volume = volume
#         self.channel = channel
#     def up_volume(self,volume):
#         self.volume += volume
#     def down_volume(self,volume):
#         self.volume -= volume
#     def up_channel(self,channel):
#         self.channel += channel
#     def down_channel(self,channel):
#         self.channel -= channel            
# # 철수-화이트,채널 10변경,2증가
# t1 = Tv() #객체선언 - 제품생산
# t1.color = "화이트"
# t1.size = 65
# t1.volume = 0
# t1.channel = 10
# t1.up_channel(2)
# print(f"철수 TV : {t1.color}, {t1.size}, {t1.volume}, {t1.channel}")
# # 영희-핑크,채널 7, 채널 5증가
# t2 = Tv("핑크",65,0,7)
# print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")
# t2.up_channel(5)
# print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")
# # 반장-실버,채널 1, 채널 3증가
# t3 = Tv("실버",65,0,1)
# print(f"반장 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")
# t3.up_channel(3)
# print(f"반장 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")

