#9.1
try:
    a, b = input('두 수를 입력하세요: ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력 오류입니다. 두 개의 수를 다시 입력하세요.")
else:
    print("결과:", result)

#9.5
with open("number1to10.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

#9.9
with open("coord.txt", "r") as file:
    n = int(file.readline())  
    points = []

    for _ in range(n):
        x, y = map(int, file.readline().split())
        points.append((x, y))

points.sort(key=lambda p: (p[0], p[1]))

for point in points:
    print(point[0], point[1])
