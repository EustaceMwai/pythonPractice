# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
x = 10
print(x)
mylist = [25, 25, "eustero"]
print(mylist)

courses = {1: "python", 2: "flutter"}
print(courses.get(1))

count = 0
while count < 9:
    print("number is:", count)
    count += 1
print("done")

import os

file = open("C:/Users/USER/Desktop/eustero.txt", 'r')
print(file.read())
file.close()

#
# x = int(input("please key in a number: "))
# if x < 0:
#     x = 0
#     print("number changed to zero")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Single")
# else:
#     print("more")



words = ["python", "flutter", "dart"]
for w in  words:
    print(w, len(w))

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(10)
#
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# ask_ok(4)

while True:
    try:
        x = int(input("please enter a number: "))
        break
    except ValueError:
        print("invalid number try again")
