#6.1
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
print(list_ex[low])
print(list_ex[low+2])
print(list_ex[high-low])
print(list_ex[low-high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2*3])
print(list_ex[2]*3)
print(list_ex[5%4])
print(len(list_ex))

#6.3
list1=[3,5,7]
list2=[2,3,4,5,6]

for i in list1:
    for j in list2:
        print('{}*{}={}' .format(i,j,i*j))
    print('')

#6.5
list1=['I like ','I love ']
list2=['pancakes.','kiwi juice.','espresso.']

for i in list1:
    for j in list2:
        print('{}' .format(i+j))
    print('')

#6.7
n_list=[10,20,30,50,60]
x=0

for i in n_list:
    x+=i

print('리스트 원소들 :',n_list)
print('리스트 원소들의 합 :',x)

#6.9
n_list=[10,20,30,50,60]
m=n_list[0]

for i in n_list:
    if i>m:
        m=i

print('리스트 원소들 :',n_list)
print('리스트 원소들 중 최댓값 :',m)

#6.11
n_list=list(map(int,input('5개의 수를 입력하세요: ').split()))

sum=0
for i in n_list:
    sum+=i
print('합 :',sum)

mean=sum/len(n_list)
print('평균 :',mean)

m=n_list[0]
for i in n_list:
    if i>m:
        m=i
print('최댓값 :',m)

n=n_list[0]
for i in n_list:
    if i<n:
        n=i
        n=i
print('최솟값 :',n)

#6.15
greet='Have a beautiful day.'
print(greet[0:4])
print(greet[7:16])
print(greet[17:20])

#6.17
animals='dog, cat, tiger, lion'
animal_list=animals.split(',')
print('animals=',animal_list)
print('animals=',animal_list [1:]+animal_list [0:1])

animals=['dog', 'cat', 'tiger', 'lion']
print('animals =',animals)

for animal in animals:
    print('I love',animal,',')

#6.19
s_list=['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list=[]

for i in s_list:
    if i not  in new_s_list:
        new_s_list.append(i)
print('s_list=',s_list)
print('new_s_list=',new_s_list)

#6.21
src="a2b3c6a2c3f1g1"
def unzips(a):
    b=""
    for i in range(1,len(a),2):
        for j in range(0,int(a[i])):
            b+=a[i-1]
    print(b)
unzips(src)

#6.23
person1=['온달',20,1,180.0,100,0]
person2=['이사부',25,1,170.0,70.0]
person3=['평강',22,0,169.0,60.0]
person4=['혁거세',40,1,150.0,50.0]

person_list=person1+person3+person4
def how_many_persons(person_list):
    return int(len(person_list)/5)
print(str(how_many_persons(person_list))+'명의 정보가 담겨 있습니다.')

person_list=person1+person2+person3+person4

def how_many_persons(person_list):
    return int(len(person_list)/5)

def compute_average_age(person_list):
    age = person_list[1::5]

    return sum(ages)/len(ages)

print('평균 나이는',str(compute_average_age(person_list)),'세입니다.')

person_list=person1+person3+person4
def how_many_persons(a):
    sex=a[2::5]
    male=sex.count(1)
    female=sex.count(0)

    print('리스트에는 남자가 {} 명, 여자가 {} 명입니다.'.format(male,female))

how_many_persons(person_list)

person_list=person1+person3+person4
def display_persons(a):
    for i in range(0,len(a),5):
        print(a[i:i+5])

display_persons(person_list)
