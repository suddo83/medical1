txt = '파이썬 파일 중에 a.txt 가 파이썬 폴더에 존재합니다.'
print(txt.find('자바'))     # 없으면 -1 리턴
print(txt.find('.'))        # 있으면 위치값 리턴
print(txt.count('파이썬'))        # 전체 있는 갯수 출력
print(txt.count('파이썬'))        # 없으면 0
print(txt.endswith('.hwp'))       # 제일 뒤에 해당문자열로 끝나면 True
txt = '파이썬 파일 중에 a.txt 가 파이썬 폴더에 존재합니다.'
print(txt.find('자바'))     # 없으면 -1 리턴
print(txt.find('.'))        # 있으면 위치값 리턴
print(txt.count('파이썬'))        # 전체 있는 갯수 출력
print(txt.count('파이썬'))        # 없으면 0
print(txt.endswith('.hwp'))       # 제일 뒤에 해당문자열로 끝나면 True
print(txt.endswith('.'))          # 제일 뒤에 해당문자열로 끝나지 않으면 False