#синтаксис базовых срезов
# pir="Python-cool!"
# print(pir[1:3]) #yt
# print(pir[-5:-2]) #coo
# print(pir[-5:11]) #cool
# print(pir[:6]) #Python
# print(pir[:-1]) #Python-cool
# print(pir[6:]) #-cool!
# print(pir[-5:]) #cool!
# пример
# myStr="1234567890"
# print(myStr[2:8:2]) #357
# print(myStr[8:2:-2]) #975
# print(myStr[::-1]) #0987654321
# print(myStr[5::2]) #680
# print(myStr[-1::-2]) #08642
# print(myStr[:len(myStr):3]) #1470
#+++++++++++++++++++++++++++++++++++++++++++++++++++++


#\n — переход на начало новой строки (newline). С помощью данной комбинации мы можем переносить следующий за ним фрагмент на новую строку

# myStr="There is no shortage of material to learn Python.\nThe following books might serve"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# \t — горизонтальная табуляция (вывод последующих
# символов начнется с отступом по горизонтали)

# print("Python books:")
# print("\t'Python Programming: An Introductionto Computer Science'")
# print("\t'The Python Guide for Beginners'")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# \x — признак шестнадцатеричного код символа, например, \x2C — это представление шестнадцатеричного
# кода символа запятой

# myStr="\x2C"
# print(myStr)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Символ «\» используется (занят) экранированными
# последовательностями, однако есть ситуации, когда нам
# нужно его отобразить в строке именно, как символ «\».
# \\ — для отображения символа «\»;
# \’ — для отображения символа апострофа;
# \» — для отображения символа двойных кавычек.

# print("\"Python Programming: An Introduction toComputer Science\"")
# print("15\\2")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# «Сырые»

# normalText='''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n'''
# rawText=r'''Python Arithmetic Operators:\n
#  Arithmetic operators are used to perform
#  mathematical operations like addition,
#  subtraction, multiplication and division.\n
#  \tThere are 7 arithmetic operators in Python:
#  \t\tAddition +\n
#  \t\tSubtraction -\n
#  \t\tDivision /\n
#  \t\tModulus %\n
#  \t\tExponentiation **\n
#  \t\tFloor division //\n
#  '''
# print(normalText)
# print(rawText)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Форматированный вывод

# userLogin=input("Your login: ")
# print("Welcome,", userLogin, ". Let's start game!")
# strMsg="Dear, "+userLogin+". Game over!"
# print(strMsg)

# str — строка-шаблон с заполнителем {} (место в шаблоне, куда следует поместить значение, переданноеаргументом метода)
# value  — аргмент-значение, которое будет подставляться в указанное место строки-шаблона

# userLogin=input("Your login: ")
# strMsg="Welcome, {}. Let's start game!".format(userLogin)
# print(strMsg)

# При этом заполнители можно идентифицировать с помощью именованных индексов {indexName}, нумерованных индексов {index} или оставить пустыми {}, как
# в примере выше
#пример:
# strMsg = "My name is {}, I'm {}".format("Student",25)
# print(strMsg)

# В случае использования пустых заполнителей {} в них
# будут подставлены аргументы метода format() четко в том
# порядке, как они перечислены в методе.

# strMsg = "My name is {}, I'm {}".format(25,"Student")
# print(strMsg) # My name is 25, I'm Student

#страница 48,табл1

# userNumber = int(input("Your number? ")) #255
# myStrB = "The binary representation of a number {n}is {n:b}".format(n=userNumber)
# print(myStrB) #The binary representation of a number255 is 11111111
# myStrO="The octal representation of a number {n}is {n:o}".format(n=userNumber)
# print(myStrO) #The octal representation of a number255 is 377
# myStrH="The Hex representation of a number {n}is {n:x}".format(n=userNumber)
# print(myStrH) #The Hex representation of a number255 is ff

#страница 49,табл2

# myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
# print(myStr1) #The number1 range from -10 to 10
# myStr2="The number2 range from {0:+} to {1:+}".format(-20,50)
# print(myStr2) #The number2 range from -20 to +50
# myStr3="The number3 range from {0: } to {1:}".format(-30,30)
# print(myStr3) #The number3 range from -30 to 30

#страница 49,табл3

#установим доступное пространство для значения до 10 символов.
# myStr1 = "You have {:<10} points."
# print(myStr1.format(12)) #You have 12 points.
# myStr2 = "You have {:>10} points."
# print(myStr2.format(12)) #You have 12 points.
# myStr3 = "You have {:^10} points."
# print(myStr3.format(12)) #You have 12 points.

# При выравнивании чисел после типа форматирования можно указывать спецификатор

# myStr1 = "Number is {:<10.2f}!"
# print(myStr1.format(34.8256)) #Number is 34.83 !
# myStr2 = "Number is {:>10.2f}!"
# print(myStr2.format(34.8256)) #Number is 34.83!
# myStr3 = "Number is {:^10.2f}!"
# print(myStr3.format(34.8256)) #Number is 34.83 !

# Рассмотренные типы форматирования также полезны
# при выравнивании строк:

# myStr1 = "Your login is {:<20}!"
# print(myStr1.format("Admin")) #Your login is Admin !
# myStr2 = "Your password is {:>20}!"
# print(myStr2.format("12345")) #Your password is 12345!
# myStr3 = "Your secret word is {:^15}!"
# print(myStr3.format("IT")) #Your secret word is IT !
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Модуль string

# import string
# import random
# userLogin = "".join(random.sample((string.ascii_lowercase),6))
# userPass = "".join(random.sample((string.ascii_letters +
#  string.digits), 8))
# print("login:",userLogin)
# print("password:",userPass)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# библеотека re

# import re
# userStr="abcd abc efgh"
# match = re.search(r'\w{4}', userStr)
# print(match.group()) # abcd
# print(match.group(0)) # abcd

#+++

# Шаблон: ‘\d{3}’

# import re
# userStr="abcd abc 123 efgh 456"
# match = re.search(r'\d{3}', userStr)
# print(match.group()) # 123

###########################################################################

#Списки

#Понятие классического массива

#Создание списков
# category =["Drama", "Comedy", "Fantasy"]
# courses =list(("Math", "Algorithms", "Databases"))
# print(category)
# print(courses)
#+++++++++++

# studentScores=[]
# students=list()
# print(studentScores) #[]
# print(students) #[]

# Также элементом списка может быть другой список:
# nestedList=[1,2.5,[45, "Example"]]
# print(nestedList) #[1, 2.5, [45, 'Example']]

# Элементы списка могут повторяться:
# customers=['Bob','Anna','Joe','Bob','Nick']

#функции list()

# mySymbols=list("abcdef")
# print(mySymbols) #['a', 'b', 'c', 'd', 'e', 'f']


# list1=[i*i for i in range(6)]
# print(list1) #[0, 1, 4, 9, 16, 25]
# В этом примере:
# i*i  — это выражение, используемое для получения квадрата числа;
# i — каждый элемент из последовательности 0, 1, 2, 3,4, 5 (sequence), которая была получена в результате
# работы функции range(6).

#++++++++

# list2=[i+"*" for i in "example"]
# print(list2) #['e*', 'x*', 'a*', 'm*', 'p*', 'l*', 'e*']

# 5 раз символов строки:
# list3=[i*5 for i in "abcdtf"]
# print(list3) #['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'ttttt', 'fffff']


# Допустим, что нам необходимо сгенерировать список из квадратов четных чисел в диапазоне от 1 до 10:
#
# list4=[i*i for i in range(1,11) if i%2==0]
# print(list4) #[4, 16, 36, 64, 100]

# Или выбрать из уже имеющегося списка всех клиентов, кроме Bob и Joe:
#
# customers=['Bob','Anna','Joe','Bob','Nick']
# list5=[i for i in customers if i!='Bob' and i!='Joe']
# print(list5) #['Anna', 'Nick']

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Работа со списками

# myList =["user", 12, 200.34, False, True]
# print(myList [1]) #12
# print(myList [-1]) #True
# print(myList [len(L)-1]) #True
# print(myList [-2]) #False

# Рассмотрим работу с различными вариантами срезов списка на примерах:

# myCourses= ["Algorithms", 2345, 7009, "Networks",
#  "Databases"]
# print(myCourses[1:3]) #[2345, 7009]
# print(myCourses[-4:-2]) #[2345, 7009]
# print(myCourses[1:-1]) #[2345, 7009, 'Networks']
# print(myCourses[:-1]) #['Algorithms', 2345, 7009,'Networks']
# print(myCourses[3:]) #['Networks', 'Databases']
# print(myCourses[::2]) #['Algorithms', 7009,'Databases']
# print(myCourses[::-1]) #['Databases', 'Networks', 7009, 2345, 'Algorithms']
# print(myCourses[-4::-1]) #[2345, 'Algorithms']

#В отличие от строк списки — это изменяемая коллекция, т.е. с использованием индекса мы можем изменять значение элемента:

# category =["Drama", "Comedy", "Fantasy"]
# print(category) #['Drama', 'Comedy', 'Fantasy']
# category[-1]="Action"
# print(category) #['Drama', 'Comedy', 'Action']

