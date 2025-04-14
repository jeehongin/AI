#8.1
from datetime import date

start_date = date(2019, 2, 14)

today = date.today()

days_elapsed = (today - start_date).days

print(f"춘향이와 몽룡이의 연애 시작일 : {start_date.year}년 {start_date.month}월 {start_date.day}일")
print(f"연애 시작일로부터 경과한 날짜 : {days_elapsed}일")

#8.5
import math

for degree in range(0, 181, 10):
    rad = math.radians(degree)  
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    try:
        tan_val = math.tan(rad)
    except:
        tan_val = float('inf') 

    print(f"sin({degree}) = {sin_val:.3f}, cos({degree}) = {cos_val:.3f}, tan({degree}) = {tan_val:.3f}")

#8.9
import random

x = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("1~20까지의 숫자를 입력하세요: "))
    attempts += 1

    if guess > x:
        print(f"{guess} 보다 작습니다.")
    elif guess < x:
        print(f"{guess} 보다 큽니다.")
    else:
        if attempts <= 3:
            print(f"{attempts}번만에 맞춘 당신은 천재!!")
        elif attempts <= 6:
            print(f"{attempts}번만에 맞추셨네요. 잘했어요^^")
        else:
            print(f"{attempts}번만에 맞추셨네요. ㅠㅠ")
        break
