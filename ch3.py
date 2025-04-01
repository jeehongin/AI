#4.1
for i in range(1,10):
    print(f"2*{i}={2*i}")

i=1
while i<10:
    print(f"2*{i}={2*i}")
    i+=1

#4.3
for i in range(3):
    print('Python')
    print('is')
    print('FUN!')

for i in range(3):
    print('Python')
    print('is')
print('FUN!')

for i in range(3):
    print('Python')
print('is')
print('FUN!')

#4.5
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

while True:
    choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력): ")

    if choice == 'b':
        print("햄버거를 선택하였습니다.")
        break
    elif choice == 'c':
        print("치킨을 선택하였습니다.")
        break
    elif choice == 'p':
        print("피자를 선택하였습니다.")
        break
    else:
        print("메뉴를 다시 입력하세요")

#4.7
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("숫자를 입력하세요 : "))

if is_prime(n):
    print(f"{n}는 소수입니다")
else:
    print(f"{n}는 소수가 아닙니다")

#4.9
n = int(input("숫자를 입력하세요 : "))
sum_of_squares = sum(i**2 for i in range(1, n+1))

print(f"결과는 {sum_of_squares}입니다.")

#4.11
depth_of_well = 30
climb_up = 7
slide_down = 5

current_height = 0
days = 0

while current_height < depth_of_well:
    days += 1
    current_height += climb_up

    print(f"day : {days}   달팽이의 위치 : {current_height}미터")
    if current_height >= depth_of_well:
        break
    current_height -= slide_down

print(f"우물을 벗어나는데 걸린 시간은 {days}일입니다.")

#4.13
armstrong_numbers = []

for num in range(100, 1000):  
    hundreds = num // 100
    tens = (num // 10) % 10        
    ones = num % 10

    if (hundreds**3 + tens**3 + ones**3) == num:
        armstrong_numbers.append(str(num))

print("세 자리의 암스트롱 수 :", " ".join(armstrong_numbers))

#4.15
fuel_tank = 500

while True:
    fuel_change = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ")
    
    try:
        fuel_change = int(fuel_change) 
    except ValueError:
        print("잘못된 입력입니다. 숫자와 +/- 기호로 입력해 주세요.")
        continue

    fuel_tank += fuel_change
    print(f"현재 탱크양은 {fuel_tank} 입니다.")

    if fuel_tank < 0.1 * 500:
        print("경고 : 연료가 10% 미만이니 충전하세요!")
        break

#4.17
def sum_of_divisors(n):
    divisors_sum = 1  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            divisors_sum += i
            if i != n // i: 
                divisors_sum += n // i
    return divisors_sum
for num in range(1, 20001):
    partner = sum_of_divisors(num)
    
    if partner > num and sum_of_divisors(partner) == num:
        print(f"{num}의 친화수 {partner}")

    
