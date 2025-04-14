#5.1
def my_greet():
    print('환영합니다.')

my_greet()
my_greet()

#5.5
def inch2cm(inch):
    return inch * 2.54

for i in range(1, 6):
    cm = inch2cm(i)
    print(f"{i} 인치 = {cm:.2f} 센티미터")

#5.9
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

input_str = input("정수를 여러 개 입력하시오 : ")
nums = list(map(int, input_str.split()))

print(f"평균값은 {mean_of_n(nums):.1f}")
print(f"최댓값은 {max_of_n(nums)}")
print(f"최솟값은 {min_of_n(nums)}")

#5.13
import math

PI = 3.14

def cube_volume(s):
    return s ** 3

def cuboid_volume(w, h, l):
    return w * h * l

def cone_volume(r, h):
    return (1/3) * PI * r**2 * h

def sphere_volume(r):
    return (4/3) * PI * r**3

def cylinder_volume(r, h):
    return PI * r**2 * h

print("모서리 길이가 12인 정육면체:", cube_volume(12))
print("모서리 길이가 20인 정육면체:", cube_volume(20))
print("가로, 세로, 깊이가 각각 3, 5, 6인 직육면체:", cuboid_volume(3, 5, 6))
print("반지름과 높이가 각각 20, 10인 원뿔:", cone_volume(20, 10))
print("반지름이 15인 구:", sphere_volume(15))
print("반지름과 높이가 각각 20, 10인 원기둥:", cylinder_volume(20, 10))

#5.17
def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))

print("{}에서 {}까지의 정수의 합 : {}".format(10, 20, sum_range(10, 20)))
print("{}에서 {}까지의 정수의 합 : {}".format(40, 100, sum_range(40, 100)))

#5.21
def parse_rrn_date(rrn):
    year = int(rrn[:2])
    month = int(rrn[2:4])
    day = int(rrn[4:6])

    if year >= 50:
        year += 1900
    else:
        year += 2000

    return "{}년 {}월 {}일".format(year, month, day)

rrn = input("주민등록번호 첫 6숫자 형식 입력 : ")
print(parse_rrn_date(rrn))

#5.25
s1 = 'Kang Young Min'
s2 = 'Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

names = [s1, s2, s3, s4]

for s in names:
    modified = s.replace(" ", "").replace("-", "").upper()
    print("{}(은)는 {}(으)로 수정됨".format(s.strip(), modified))
    
print()

for s in names:
    modified = s.replace(" ", "").replace("-", "").upper()
    n_count = modified.count('N')
    print("{} : {}개의 N이 나타남".format(modified, n_count))
