
# 두 수를 입력받아서 사칙연산을 출력해보세요
# 예: 30, 6을 입력받아서
# 출력 : 
# 30 + 6 = 36
# 30 - 6 = 30
# 30 * 6 = 180
# 30 / 6 = 5.0

a = int(input("첫번째 숫자를 입력하세요 >> "))
b = int(input("두번째 숫자를 입력하세요 >> "))

# print (int(a),'+', int(b),'=',int(a)+int(b))
# print (int(a),'-', int(b),'=',int(a)-int(b))
# print (int(a),'*', int(b),'=',int(a)*int(b))
# print (int(a),'/', int(b),'=',int(a)/int(b))
# 입력함수에서 변수선언으로 인해 미사용

print('{}+{}={}'.format(a,b,a+b))
print('{}-{}={}'.format(a,b,a-b))
print('{}*{}={}'.format(a,b,a*b))
print('{}/{}={}'.format(a,b,a/b))

# print('%d+%d=%d'%(int(a),int(b),int(a)+int(b)))
# print('%d-%d=%d'%(int(a),int(b),int(a)-int(b)))
# print('%d*%d=%d'%(int(a),int(b),int(a)*int(b)))
# print('%d/%d=%d'%(int(a),int(b),int(a)/int(b)))
# 입력함수에서 변수선언으로 인해 미사용
