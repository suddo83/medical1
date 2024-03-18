# 파일열기
with open('medical_1.csv', 'r', encoding='utf8') as f:
    # 파일읽기
    list1 = []
    next(f)  # 첫 번째 줄은 헤더이므로 건너뜁니다.
    for line in f:
        line = line.strip()  # 줄 끝의 개행문자를 제거합니다.
        if line:  # 공백 줄은 건너뜁니다.
            list1.append(line.split(','))  # 쉼표로 분리하여 리스트에 추가합니다.

# 결과 출력
for row in list1:
    print(row)
