class Car:
    car_name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0
    
    def up_speed(self,s):
        self.speed += s
        
c1 = Car()
c1.car_name = '드뉴아반떼'
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60) # 현재 speed 60을 더해 줌
c1.up_speed(40) # 현재 speed는 얼마? 100
c1.up_speed(50) # 현재 speed는 얼마? 150
c1.speed = 50   # 현재 speed는 얼마? 50

# # 영희의 차를 1대 생산해서, 색상은 green, 나머지 동일, speed = 100 설정해서 출력하시오.
c2 = Car()
c2.car_name = '드뉴아반떼'
c2.color = 'green'
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.up_speed(100) 


print('철수차 성능 : ',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
print('영희차 성능 : ',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
