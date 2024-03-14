<<<<<<< HEAD
a_list = [1,2,3]
try:
    raise '에러발생' # 강제 에러 발생구문
    print(a_list[5])
    txt = int(input('숫자를 입력하세요.>> '))
    print(txt)
except IndexError:
    print('리스트 주소가 잘못 입력되었습니다.')
except Exception as e:
    print('-- 예외가 발생했습니다.')
    print('타입 :',type)
=======
a_list = [1,2,3]
try:
    raise '에러발생' # 강제 에러 발생구문
    print(a_list[5])
    txt = int(input('숫자를 입력하세요.>> '))
    print(txt)
except IndexError:
    print('리스트 주소가 잘못 입력되었습니다.')
except Exception as e:
    print('-- 예외가 발생했습니다.')
    print('타입 :',type)
>>>>>>> 992ee3a (파이썬 수업내용)
    print(e)