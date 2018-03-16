import sys
import os

# print("hello python") #주석처리
#
# age = 20
# name = 'yarak'
# sex = "male"
#
# print("{} was {} years old when he wrote this book".format(name, age, sex)),
# print("Why is {0} playing with the python?".format(name, age))
# print("Why is \n playing with the python?")
# print(r"Why is \n playing with the python?")
#
# number = 23
# running = True

# while running:
#     guess = int(input("Enter an integer: "))
#
#     if guess == number:
#         print('축하 맞쳤어')
#         running = False
#     elif guess < number:
#         print('그것보단 많아')
#     else:
#         print("그것보단 적어")
# else:
#    print("순환문 종료")
#
# print("끝")


# for i in range(1, 5):
#     print(i)
# else:
#     print("순환문 종료")
#
#
# def say_hello():
#     print("hello world")
#
# say_hello()
# say_hello()
#
# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equals to ', b)
#     else:
#         print(b, 'is maximum')
#
# print_max(3, 4)
# x = 5
# y = 7
#
# print_max(x, y)


# x = 50
#
# def func():
#     global x
#     print ("x is", x)
#     x = 2
#     print('Change local x to', x)
#
# func()
# print("x is still", x)

# def say(message, times = 1):
#     print(message * times)
#
# say("Hello")
# say("World", 5)


def total(initial = 5, *numbers, **keywords):
    '''Print the total of parmaters

    :param initial:
    :param numbers:
    :param keywords:
    :return:
    '''
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1,2, 3, vegetables=50, fruits=100))
print(total.__doc__)
help(total)



print("The commmand line arguments are: ")
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

print(os.getcwd())


from math import sqrt
print("Square root of 16 is", sqrt(16))

if __name__ == '__main__':
    print("this program is being run by itself")
else:
    print("I am being imported from another module")
print(__name__)
