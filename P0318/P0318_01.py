 # 클래스 : 사용자정의 변수 - 함수도 포함
 # 클래스 첫글자 대문자 사용
 # 클래스 : 설계도
class Car:
    color = 'white'
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp
        
        
        
# 객체선언을 할때마다 제품(car)이 한개씩 생산

c1 = Car() # 객체선언

c2 = Car()