def cal(num1, num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    if num2 != 0:
        r_list[5] = num1 / num2
    else:
        r_list[5] = "나눗셈 오류: 두 번째 숫자가 0입니다."
    return r_list

save_list = []
while True:
    num1 = int(input("1번째 숫자를 입력하세요.>> (0.종료)"))
    if num1 == 0:
        break
    num2 = int(input("2번째 숫자를 입력하세요.>> "))
    result = cal(num1, num2)
    save_list.append(result)
    print(f'{result[0]},{result[1]} 결과값 : {result[2]},{result[3]},{result[4]},{result[5]}')


print('[ 현재까지 입력한 숫자,결과값 ]')
for i in range(len(save_list)):
def cal(num1, num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    if num2 != 0:
        r_list[5] = num1 / num2
    else:
        r_list[5] = "나눗셈 오류: 두 번째 숫자가 0입니다."
    return r_list

save_list = []
while True:
    num1 = int(input("1번째 숫자를 입력하세요.>> (0.종료)"))
    if num1 == 0:
        break
    num2 = int(input("2번째 숫자를 입력하세요.>> "))
    result = cal(num1, num2)
    save_list.append(result)
    print(f'{result[0]},{result[1]} 결과값 : {result[2]},{result[3]},{result[4]},{result[5]}')


print('[ 현재까지 입력한 숫자,결과값 ]')
for i in range(len(save_list)):
    print(f'{save_list[i][0]},{save_list[i][1]} 결과값 : {save_list[i][2]},{save_list[i][3]},{save_list[i][4]},{save_list[i][5]}')