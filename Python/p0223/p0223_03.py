# 조건문
# 1. 키가 130cm 이상만 놀이기구를 탑승할 수 있다.
height = 120
# 조건문
if height < 130:
    print("못탐")
else:
    print("탐")

# 2. 나이가 10살 이상이고 키가 130 이상만 놀이기구 탑승가능
age = 11

if height >= 130 and age >= 10:
    print("탐")
else:
    print("못탐")

# 3. 비 면 [우산을 챙겨주세요]
# 아니면 [선크림 발라주세요] 출력
weather = '비'

if weather == "비":
    print("우산을 챙겨주세요")
else:
    print("선크림 발라주세요")

# 4. 비나 눈이면 [우산을 챙겨주세요]
# 아니면 [선크림발라주세요] 출력

if weather == "비" or weather == "눈":
    print("우산을 챙겨주세요")
else:
    print("선크림 발라주세요")