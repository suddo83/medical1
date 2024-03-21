# 2차원 리스트 생성방법
# [
#       [0],[0],[0]...... 52개를 생성하시오.
# ]
aa = [[0]*2]*52 # 얕은 복사이기에 쓸수 없음.

bb = [[0]*2 for i in range(52)]
print(bb)

cc = []
for i in range(52):
    dd = []
    for j in range(2):  # range값을 변경하면 리스트 길이를 수정가능
        dd.append(0)
    cc.append(dd)
print(cc)


# aa[0][0] = 1
# print(aa)
# # 1차원 리스트 생성방법
# # [0,0,0,0,0,0 ..... 52개를 생성하시오.]
# a_list = [0]*52
# b_list = []
# for i in range(52):
#     b_list.append(0)

# c_list = [0 for i in range(52)]

# print(a_list)
# print(b_list)
# print(c_list)

