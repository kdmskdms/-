import numpy as np

#1

print("1.다음 함수의 결과값을 예측하시오.")

'''
def ex1():
    num1 = 2
    num2 = 4
    total = num1*num2+num1-num2
    return

print(ex1())
'''
print("="*50)
print(None)

#2
print("2.def 함수를 이용하여 입력값이 홀수인지 짝수인지 판별하는 함수를 작성하시오.")

number = int(input("숫자를 입력하세요."))
def is_odd_or_even(number):
    if number%2 == 1:
        print("홀수입니다.")
    elif number%2 == 0 :
        print("짝수입니다.")

is_odd_or_even(number)

#3
print("3.for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하시오.")
print('''
오늘의 메뉴: 김밥
오늘의 메뉴: 라면
오늘의 메뉴: 튀김
''')
List1=["김밥","라면","튀김"]

for food in List1:
    print("오늘의 메뉴 : ",food)
print("="*50)
#4
print("4.list에 있는 동물이름과 글자수를 출력하시오.")
print('''
List:
dog 
cat 
parrot
      ''')
print("="*50)
list_animal = ["dog","cat","parrot"]

for name in list_animal:
    print(name, len(list(name)))

#5
print("5.월드컵은 4년에 한번씩 개최된다. 2002년부터 2050년까지 월드컵이 개최되는 연도를 출력하시오.")

for x in range(2002, 2051, 4) :
    print ("%i년" %x)
print("="*50)
#6
print("6.숫자를 n개 입력받아 짝수만 출력하는 함수를 정의하시오.")
list_number1 = []
list_even =[]
def print_even(list_number1):
    while True:
        value = int(input("숫자를 입력하세요. : "))
        list_number1.append(value)
        if value == -1:
            break
    for i in list_number1 :
        if i%2 == 0:
            list_even.append(i)
    print(list_even)
            
print_even(list_number1)

print("="*50)
#7
print("7.숫자를 n개 입력받아 홀수값의 평균을 출력하는 함수를 정의하시오.")

list_number2=[]

def print_odd(list_number2):
    
    list_odd =[]
    while True:
        value = int(input("숫자를 입력하세요. : "))
        list_number2.append(value)
        if value == -1:
            break
        for i in list_number2 :
            if i%2 == 1:
                list_odd.append(i)
            elif i == -1:
                list_odd.remove(-1)
    odd_set=set(list_odd)
    total = sum(odd_set)/len(odd_set)
    print(odd_set)
    print(total)            
print_odd(list_number2)

print("="*50)

#8
print("8.숫자를 n개 입력받아 전체 숫자의 분산값을 구하는 함수를 정의하시오.")
list_number3 = []
def variance(list_number3):
    while True:
        value = int(input("숫자를 입력하세요. : "))
        list_number3.append(value)
        if value == -1:
            list_number3.remove(-1)
            break
    var1 = np.var(list_number3)
    print("variance : ",var1)

variance(list_number3)

print("="*50)
#9
print("9.숫자를 n개 입력받아 전체 숫자의 표준편차를 구하는 함수를 정의하시오.")
list_number4 = []
def std_deviation(list_number4):
    while True:
        value = int(input("숫자를 입력하세요. : "))
        list_number4.append(value)
        if value == -1:
            list_number4.remove(-1)
            break
    std_dev = np.std(list_number4)
    print("standard deviation : ",std_dev)

std_deviation(list_number4)

print("="*50)













