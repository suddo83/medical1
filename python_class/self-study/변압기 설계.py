# 필요한 모듈 가져오기
import math

# 입력값 받기
Vin = float(input("입력 전압(V): "))
Vout = float(input("출력 전압(V): "))
Pout = float(input("출력 전력(W): "))
fsw = float(input("스위칭 주파수(kHz): "))
Bmax = float(input("코어 최대 자손 밀도(Bmax): "))
J = float(input("코어 최대 전류 밀도(A/mm^2): "))
Kc = float(input("적정 공간효율(%): "))
Kf = float(input("적정 주파수 비율(%): "))

# 입력값에 기반하여 계산 수행
Vd = 0.7 # 다이오드 드롭(V)
D = Vout / Vin # 듀티 사이클
Iout = Pout / Vout # 출력 전류
Iin = Iout / D # 입력 전류
Ploss = 0.1 * Pout # 손실 전력
Pc = Pout + Ploss # 코어 손실 전력
Pcore = Pc / (1 - Kc/100) # 코어 전력
Pfsw = Pcore * (Kf/100) # 코어 손실 전력의 주파수 부분
Is = Iin / 2 # 스위치 흐름 전류
Irms = Is / math.sqrt(2) # 스위치 흐름 전류의 RMS 값
Ae = Is / J # 유효적인 흐름 영역(mm^2)
Ac = Ae * 2 # 코어 단면적(mm^2)
Lm = (Vin - Vd) / (fsw * Irms) # 흐름 인덕턴스
N = math.sqrt(Lm / (Bmax * Ac)) # 덩이 수
AL = Lm / (N**2) # 핀딩 인덕턴스

# 결과 출력
print("\n디자인 결과:")
print("  - 스위치 듀티 사이클: {:.2f}".format(D))
print("  - 입력 전류 (A): {:.2f}".format(Iin))
print("  - 코어 손실 전력 (W): {:.2f}".format(Pcore))
print("  - 코어 손실 전력의 주파수 부분 (W): {:.2f}".format(Pfsw))
print("  - 스위치 흐름 전류의 RMS 값 (A): {:.2f}".format(Irms))
print("  - 코어 단면적 (mm^2): {:.2f}".format(Ac))
print("  - 필요한 핀딩 인덕턴스 (nH): {:.2f}".format(AL * 1e9))
print("  - 코어 덩이 수: {:.0f}".format(N))