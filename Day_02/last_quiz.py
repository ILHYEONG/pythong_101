# 태어난 년도 입력하고 현재 만나이 출력
a = int(input('당신의 태어난 년도는?'))
age = 2023-a
print(f"당신의 만나이는 {age}입니다.")

# 세 개의 숫자 평균 계산기
b = int(input("첫번째 숫자 입력 : "))
c = int(input("두번째 숫자 입력 : "))
d = int(input("세번째 숫자 입력 : "))
avg = (b+c+d) / 3
print(f"평균은 {avg}입니다.")

# 환율 계산기
d = int(input("원화금액 입력하세요"))
dollar = d*0.00077
yen = d*0.11
print(f"달러는 {dollar}달러이고, 엔화는 {yen}엔이네요")

# 거리 변환기
e = float(input("킬로미터 거리입력하세요 "))
mile = e*0.621371
print(f"거리는 {mile}마일입니다.")

# 체온 변환기
f = float(input("섭씨 온도 몇도에요?"))
fasi = f*59+32
print(f"화씨로 환산하면 {fasi}화씨입니다.")

# 체질량 지수(BMI) 계산기
g = float(input("키는 몇m입니까?"))
h = float(input("몸무게는 몇kg이에요"))
bmi = h/(g**2)
print(f"당신의 BMI지수는 {bmi}입니다. ")

# 여행시간 계산기
i = float(input("여행거리는 몇키로미터?"))
j = float(input("속도?"))
time = i / j
print(f"도착까지 걸리는 시간은 {time}시간입니다.")

#반지름을 입력 받을 때 원의 둘레를 출력하는 프로그램
r = float(input("반지름을 입력하세요"))
print(f"원의 둘레는 {2*3.141592*r}입니다.")

#반지름을 입력 받을 때 원의 넓이를 출력하는 프로그램
print(f"원의 넓이는 {3.141592*r*r}입니다.")

#반지름을 입력 받을 때 구의 부피를 출력하는 프로그램
print(f"구의 부피는는 {(4/3)*3.141592*r*r*r}")

#한 변의 길이를 입력하고 정사각형의 둘레와 넓이를 출력하는 프로그램
l = float(input("한변의 길이를 입력하세요"))
print(f"정사각형의 둘레는 {4*l}이고 넓이는 {l*l}입니다.")