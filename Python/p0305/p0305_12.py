import operator

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}
t_list = sorted(t_dic.items(),key = operator.itemgetter(0),reverse=True)
print(t_list)
# (peach,복숭아),(orange,오렌지)....

print(t_dic.keys())   # 키값
print(t_dic.values()) # value값
print(t_dic.items())  # 튜플

# # 3개의 숫자를 입력받아 순서대로 출력하시오.
# # 17,50,12
# num = [0,0,0]
# for i in range(3):
#     print(i)
#     num[i] = int(input(f'{i+1}숫자입력>> '))
#         # input('{}번째 숫자를 입력하세요.'.format(i+1))
# # num.sort()
# print('최대값 : ',max(*num))
# print('최소값 : ',min(*num))
# print(num)
# # 12,17,50
# a2 = int(input('숫자입력>> '))
# a2.sort(reverse=True) # 역순정렬
# # a = [5,7,4,8,1,9,3,2]
# # a.sort() # 순차정렬
# # print(a)
# # print('-'*50)
# # b = [5,7,4,8,1,9,3,2]
# # b.sort(reverse=True) # 역순정렬
# # print(b)