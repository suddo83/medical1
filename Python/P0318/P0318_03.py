class Car:
    car_name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0
    
    # 생성자
    def __init__(self,car_name='',color='',door=5,length=1000,width=1000,speed=0):
        self.car_name = car_name
        self.color = color
        self.door = door
        self.length = length
        self.width = width
        self.speed = speed
    
    def up_speed(self,s):
        self.speed += s

# 기본생성자를 사용한 객체선언
c4 = Car()
c4.car_name = '드뉴아반떼'
c4.color = 'green'
c4.door = 5
c4.length = 2000
c4.width = 1000
c4.up_speed(100) 
print('기본 성능 : ',c4.car_name,c4.color,c4.door,c4.length,c4.width,c4.speed)

# 생성자를 사용한 객체선언 = 인스턴스 선언
c1 = Car('드뉴아반떼','white',5,200,1000,60)
print('철수차 성능 : ',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2 = Car('드뉴아벤떼','green',5,200,1000,100)
print('영희차 성능 : ',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

# c1 = Car()
# c1.car_name = '드뉴아반떼'
# c1.color = 'white'
# c1.door = 5
# c1.length = 2000
# c1.width = 1000
# c1.up_speed(60) 
# c1.up_speed(40) 
# c1.up_speed(50) 
# c1.speed = 50   

# c2 = Car()
# c2.car_name = '드뉴아반떼'
# c2.color = 'green'
# c2.door = 5
# c2.length = 2000
# c2.width = 1000
# c2.up_speed(100) 

