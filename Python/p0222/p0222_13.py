#1. 숫자를 입력받아서 양수면 양수 아니면 음수를 출력

n = int(input("숫자입력 >> "))
if n > 0:
    print("양수")
else:
    print("음수")
if n == 0:
    print("0입니다")
else:
    print("0이 아닙니다")
        
print("End")