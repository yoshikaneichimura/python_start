import random

"""構文"""
# This is a comment.

# print("Hello, World!")

# if 5 > 2:
#     print("Five is greater than two!")

# x = 5
# y = "Hello, World!"

"""出力"""

# print("Hello World!")
# print("Have a good day.")
# print("Learning Python is fun!")

# print("Hello"); print("How are you"); print("Bey bye!")

# print("Hello World")
# print("I am learning Python.")
# print("It is awesome!")

# print("This will work!")
# print('This will also work!')

# print("Hello World!", end=" ")
# print("I will print on the same line.")

# print(3)
# print(358)
# print(50000)

# print(3 + 3)
# print(2 * 5)

# print("I am", 35, "years old.")

#print("Hello, World!") #This is a comment 

# print("Cheers, Mate!")

# This is comment
# written in 
# more than just one line

# print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
# print("Hello World!")
"""変数"""

# x = 5
# y = "John"
# print(x)
# print(y)

# x = 4
# x = "Sally"

# print(x)

# x = str(3)
# y = int(3)
# z = float(3)

# print(x); print(y); print(z)
# print(type(x)); print(type(y)); print(type(z)) 

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# x = "John"
# is the same as
# x = 'John'

# print(x)

# a = 4
# A = "Sally"

# print(a); print(A)

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# myvar2 = "John"

# print(myvar); print(my_var); print(_my_var); print(myVar); print(myvar2)

# MyVariableName = "John"
# my_variable_name = "John"

# print(MyVariableName); print(my_variable_name)

# x, y, z = "Orange", "Banana", "Cherry"
# print(x); print(y), print(z)

# x = y = z = "Orange"
# print(x); print(y); print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x); print(y); print(z)

# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# x = "awesome" #グローバル関数

# def myfunc():
#     print("Python is " + x)

# myfunc()

# x = "awesome" # グローバル変数

# def myfunc():
#     x = "fantastic" # ローカル変数
#     print("Python is " + x)

# myfunc()
# print("Python is " + x)

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

# x = "awesome"

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

"""データ型"""
# x = 1
# y = 2.8
# z = 1j

# print(type(x)); print(type(y)); print(type(z))

# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x)); print(type(y)); print(type(z))

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x)); print(type(y)); print(type(z))

# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x)); print(type(y)); print(type(z))

# x = 3+5j
# y = 5j
# z = -5j

# print(type(x)); print(type(y)); print(type(z))

# x = 1
# y = 2.8
# z = 1j

# a = float(x)
# b = int(y)
# c = complex(x)

# print(a, b, c)
# print(type(a)), print(type(b)), print(type(c))

# print(random.randrange(1, 10))

"""キャスティング"""

# x = int(1)
# y = int(2.8)
# z = int("3")

# print(x, y, z)
# print(type(x)), print(type(y)), print(type(z))

# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")

# print(x, y, z, w)
# print(type(x)), print(type(y)), print(type(z)), print(type(w))

# x = str("s1")
# y = str(2)
# z = str(3.0)

# print(x, y, z)
# print(type(x)), print(type(y)), print(type(z))

"""文字列"""

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = "Hello"
# print(a)

# a = """Lorem ipusum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

# print(a)

# a = '''Lorem ipusum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''

# print(a)

# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#     print("No, 'expensive' is NOT persent.")

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = " Hello, World! "
# print(a.strip())

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(","))

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 36
# txt = f"My name is john, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt =f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

"""bool値"""

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than b")

# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# class myclass():
#     def __len__(self):
#         return 0

# myobj = myclass()
# print(bool(myobj))

# def myfunction() :
#     return True
# print(myfunction())

# def myfunction():
#     return True

# if myfunction():
#     print("YES!")
# else:
#     print("NO!")
# x = 200

# print(isinstance(x, int))

"""演算子"""

# print(10 + 5)

# sum1 = 100 + 50
# sum2 = sum1 + 150
# sum3 = sum2 + sum2

# print(sum1, sum2, sum3)

# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# numbers = [1,2,3,4,5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# num = 6

# x = "WEEKEND!" if num > 5 else "Workday"

# print(x)

# num = 6

# x = "Fri" if num == 5 else "Sat" if num  == 6 else "Sun" if num == 7 else "weekday"

# print(x)

# x = 5
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)

# x = 5

# print(1 < x < 10)
# print(1 < x and x < 10)

# x = 5

# print(x > 0 and x < 10)

# x = 5

# print(x < 5 or x > 10)

# x = 5

# print(not(x > 3 and x < 10 ))

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# x = ["apple", "banana"]
# y = ["apple", "banana"]

# print(x is not y)

# x = [1,2,3]
# y = [1,2,3]

# print(id(x)); print(id(y))
# print(x == y); print(x is y)

# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)

# fruits = ["apple", "banana", "cherry"]

# print("pinapple" not in fruits)

# text = "Hello World"

# print("H" in text); print("hello" in text); print("z" not in text)

# print(6 & 3)

# print(6 | 3)

# print(6 ^ 3)

# print((6 + 3) - (6 + 3))

# print(100 + 5 * 3)

# print(5 + 4 - 7 + 3)