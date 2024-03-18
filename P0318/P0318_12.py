# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo 에는 carCount 숫자를 이용해서 carNo를 넣으시오.
# carNo, color='white',door=5,tire=4,speed
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 -10씩 감소

# c1 - white,5,4,0 -> speed 30이 되도록
# c2 - red,5,4,0 -> speed 100
# c3 - silver,5,4,0 -> speed 70
# car_list 추가하고

# car_list 에 있는 모든 객체의 모든 color,door,tire,speed 모두 출력하시오.

class Car:
    carCount = 0
    carNo = 0
    color = 'white'
    door = 5
    tire = 4
    speed = 0
    
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1
        self.carNo = Car.carCount
    
    def up_speed(self,speed):
        self.speed = speed + 10
        
    def down_speed(self,speed):
        self.speed = speed - 10
        
    # def stu_print(self):
    #     print(self.carNo,self.color,self.door,self.tire,
    #         self.speed,sep='\t')
    # def __str__(self):
    #     return f'{self.carNo},{self.color},{self.door},{self.tire},{self.speed}'

c1 = Car('white',5,4,0)
c1.up_speed(20)
c2 = Car('red',5,4,0)
c2.up_speed(90)
c3 = Car('silver',5,4,0)
c3.up_speed(60)

car_list = [c1,c2,c3]
for i in range(3):
    print(f'리스트 출력 : {car_list[i].carNo},{car_list[i].color},{car_list[i].door},{car_list[i].tire},{car_list[i].speed}')





        
        
