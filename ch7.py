#7.1
price={'김밥': 5000, '어묵':3000, '떡볶이': 2000}
print (price['김밥'])
price['김밥']=6000
print(price)
print(price.values())
print(price.keys())
print(f"이 식당의 메뉴 개수는 {len(price)}개 입니다.")

#7.5
t=(10, 20, 30, 40)
print(t[0])
print(t[0:2])
print(t[1:])
print(t[:3])
print(t[1::2])
print(t[::-1])

#7.9
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
unique_tup = tuple(sorted(set(tup)))

print("주어진 튜플:", tup)
print("중복 제거 튜플:", unique_tup)

#7.13
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

n = len(lst)
for i in range(n - 1):
    for j in range(n - 1 - i):  
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("주어진 리스트는:", [5, 6, 3, 9, 2, 12, 3, 8, 7])
print("정렬된 결과는:", lst)

#7.17
population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 40, 5, 1, 1, 1, 1)

votes_A = sum(population_A[2:])
votes_B = sum(population_B[2:])

print("마을 A와 B에 보낼 투표용지의 개수는 각각 {}장과 {}장입니다.".format(votes_A, votes_B))

aging_A = sum(population_A[7:])
aging_B = sum(population_B[7:])

total_A = sum(population_A)
total_B = sum(population_B)

aging_rate_A = aging_A / total_A
aging_rate_B = aging_B / total_B

print("마을 A와 B의 고령화 정도는 각각 {:.3f}와 {:.3f}입니다.".format(aging_rate_A, aging_rate_B))

#7.21
def is_palindrome(s):
    s = s.lower()
    cleaned = ''.join(char for char in s if char.isalpha())
    return cleaned == cleaned[::-1]

text = input("문자열을 입력하세요: ")

if is_palindrome(text):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

#7.25
dictionary = {}

print("사전 프로그램 시작... 종료는 q를 입력")

while True:
    cmd = input("$ ")

    if cmd == 'q':
        print("사전 프로그램을 종료합니다.")
        break

    try:
        if cmd.startswith("k "):
            data = cmd[2:].strip()
            eng, kor = data.split(":")
            dictionary[eng.strip()] = kor.strip()

        elif cmd.startswith("v "):
            word = cmd[2:].strip()
            if word in dictionary:
                print(dictionary[word])
            else:
                print(f"{word}가 사전에 없습니다.")

        else:
            print("입력 오류가 발생했습니다.")
    except:
        print("입력 오류가 발생했습니다.")
