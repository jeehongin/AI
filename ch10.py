#10.1
result1=(123).__add__(334)
print(result1)

result2=(123).__sub__(334)
print(result2)

result3=(123).__mul__(334)
print(result3)

result4=(123).__truediv__(3)
print(result4)

#10.3


#10.5


#10.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름은 {self.name}이고 나이는 {self.age}살입니다."

my_dog = Dog("Mango", 3)

print(my_dog)

#10.9
class Counter:
    def __init__(self, number):
        self._number = number

    def __add__(self, other):
        result = self._number + other._number
        if result >= 100:
            result = 0
        return Counter(result)

    def __sub__(self, other):
        result = self._number - other._number
        if result <= -1:
            result = 0
        return Counter(result)

    def __str__(self):
        return f'C({self._number})'

c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)


#10.11
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._korean_quiz = 0
        self._math_quiz = 0
        self._science_quiz = 0
        self._total_score = 0

    def __str__(self):
        return f'이름: {self._name}, 학번: {self._student_id}\n' \
               f'국어 성적 : {self._korean_quiz}, 수학 성적 : {self._math_quiz}, 과학 성적 : {self._science_quiz} ' \
               f'합계 : {self.get_total_score()}, 평균 : {self.get_avg_score():.1f}'

    def get_name(self):
        return self._name

    def get_student_id(self):
        return self._student_id

    def get_korean_quiz(self):
        return self._korean_quiz

    def get_math_quiz(self):
        return self._math_quiz

    def get_science_quiz(self):
        return self._science_quiz

    def set_korean_quiz(self, score):
        self._korean_quiz = score
        self._update_total()

    def set_math_quiz(self, score):
        self._math_quiz = score
        self._update_total()

    def set_science_quiz(self, score):
        self._science_quiz = score
        self._update_total()

    def get_total_score(self):
        return self._total_score

    def get_avg_score(self):
        return self._total_score / 3

    def _update_total(self):
        self._total_score = self._korean_quiz + self._math_quiz + self._science_quiz

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')
student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)

#10.13
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle : (x = {self.__x}, y = {self.__y}, w = {self.__width}, h = {self.__height}), 면적 : {self.area()}"

    def set_x(self, x): self.__x = x
    def get_x(self): return self.__x

    def set_y(self, y): self.__y = y
    def get_y(self): return self.__y

    def set_width(self, width): self.__width = width
    def get_width(self): return self.__width

    def set_height(self, height): self.__height = height
    def get_height(self): return self.__height

    def area(self):
        return self.__width * self.__height

    def overlaps(self, r):
        return not (self.__x + self.__width <= r.get_x() or
                    self.__x >= r.get_x() + r.get_width() or
                    self.__y + self.__height <= r.get_y() or
                    self.__y >= r.get_y() + r.get_height())

    def contains(self, r):
        return (self.__x <= r.get_x() and
                self.__y <= r.get_y() and
                self.__x + self.__width >= r.get_x() + r.get_width() and
                self.__y + self.__height >= r.get_y() + r.get_height())

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))
