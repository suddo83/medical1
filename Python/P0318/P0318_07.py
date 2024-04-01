class TV():
    serial_no = 0 # 클래스변수
    
    def __init__(self,color,name,size):
        self.color = color
        self.name = name
        self.size = size  # 인스턴스변수
        TV.serial_no += 1 # 클래스변수 - 모든 클래스에서 공통으로 사용하는 변수
    
    def tv_print(self):
        print(f'TV : {self.serial_no},{self.color},{self.name},{self.size}')
        
        
c1 = TV('white','스마트TV',100)
c1.tv_print()

c2 = TV('black','FHDTV',70)
c2.tv_print()

c3 = TV('silver','OLEDTV',70)
c3.tv_print()