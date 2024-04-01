foods = {'떡볶이':'오뎅','짜장면':'단무지','라면':'김치',
         '피자':'피클','맥주':'땅콩','삼겹살':'상추'}
# 키의 값을 출력하시오.
print(foods.key())
for key in foods:
    print(key,end='\t')
# value 값을 출력하시오.
print(foods.values())
for value in foods():
    print(foods[key],end='\t')
# key:value 형태로 모두 출력하시오.
# print(foods)
for key, value in foods.items():
    print(f"{key} : {value}")