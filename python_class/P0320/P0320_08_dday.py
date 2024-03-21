# from datetime import datetime

# # D-Day 계산 함수
# def calculate_dday(target_date):
#     today = datetime.today()
#     dday = target_date - today
#     return dday.days

# # 메인 기능
# target_date_str = input("목표 날짜를 YYYY-MM-DD 형식으로 입력하세요: ")

# target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
# dday = calculate_dday(target_date)

# if dday > 0:
#     print(f"D-{dday} 남았습니다.")
# elif dday == 0:
#     print("D-Day입니다!")
# else:
#     print(f"D+{abs(dday)} 경과했습니다.")
#------------------------------------------------------------------------------
from datetime import datetime

def calculate_dday(target_date):
    today = datetime.today()
    dday = target_date - today
    return dday.days

def main():
    target_date_str = input("목표 날짜를 YYYY-MM-DD 형식으로 입력하세요: ")
    
    try:
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        dday = calculate_dday(target_date)
        
        if dday > 0:
            print(f"D-{dday} 남았습니다.")
        elif dday == 0:
            print("D-Day입니다!")
        else:
            print(f"D+{abs(dday)} 경과했습니다.")
    except ValueError:
        print("올바른 형식으로 날짜를 입력해주세요.")

if __name__ == "__main__":
    main()
