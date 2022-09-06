# This is a sample Python script.
import re
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"lab2 -Q1"
# def greate_array(lenth,start):
#     x=range(start,start+lenth,1)
#     x=list(x)
#     return x
# print(greate_array(5,1))
"lab2 -Q2"
# def checkdiv():
#     dig=input("enter a number")
#     if dig.isdigit():
#         dig=int(dig)
#     else:
#         return  checkdiv()
#     if dig % 3 == 0 and dig % 5 == 0:
#         print("FizzBUZZ")
#     elif dig % 3==0:
#         print("Fizz")
#     elif dig % 5==0:
#         print("Fizz")
#
# checkdiv()
"lab2 -Q3"

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# x="mohmad"
# print(reverse(x))
"lab2 -Q4"
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# def confirm():
#      name=input("enter your name :")
#      if name.isdigit()or name.strip()=="":
#          return confirm()
#      else:
#         email=input("enter your email :")
#         while True:
#             if (re.fullmatch(regex, email)):
#                 print("Valid Email")
#                 print(f"username is {name} and his email {email}")
#                 return
#
#
#             else:
#                 print("Invalid Email")
#                 email = input("enter your email :")
#
#
#
#
#
# confirm()
"lab2 -Q5"
# def lsubstr(inputString ):
#     prevChar = ""
#     currentString = ""
#     longestString = ""
#
#     for char in inputString:
#         if prevChar <= char:
#             currentString += char
#             if len(currentString) > len(longestString):
#                 longestString = currentString
#         else:
#             currentString = char
#         prevChar = char
#     print('Longest substring in alphabetical order is: ' + longestString)
#
# name=input("enter your name :")
# lsubstr(name)
"lab2 -Q6"
# count=0
# sum=0
# while True:
#     inp=input(" enter number or to exit enter done")
#     if inp=="done":
#         print(f"the total is {sum} the count is {count} the average is {sum/count}")
#         break
#     elif inp.isdigit():
#         sum+=int(inp)
#         count+=1
#     else:
#         print("invalid input ")
#         continue
"lab2 -Q7"
words =["x","y","z","d","l"]
count=7
rv=random.choice(words)
print(f"our sucess choice is {rv}")
while True :
    if(count==0):
        print("you have been failed")
        break;
    else:
        name=input("enter your word :")

        if(name==rv):
            print("Congratulation you won")
            break
        else:
            count-=1
            continue

