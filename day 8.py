'''
#eg:3

def profile(name,age,place):
    txt="my name is {}.iam {} years old.iam from {}."
    print(txt.format(name,age,place))
profile("sid",29,"cbe")

#---->function with return statement
#return

1)a variable declared inside the function can be accessed outside the function
using return
2)return does not print anything
3)we cannot write any code below return statement

def f1():
    z=8
f1()
print(z)  #error--->cannot use outside the function


def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a=input("enter the value:")
palindrome(a)
#based on the declaration of parameter and args
#functions are divided into 5 catagories

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args

#--->positional args
eg:1
def profile(phone,name,marks):
    txt="my name is {}.my phone number {}.i got {} marks."
    print(txt.format(phone,name,marks))
profile("sid",8963489754,78)


# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)

# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
profile("shashank",mark=98,phone=9876543210)
#default args
#the method of assigning the argument to the paremeter while declaring the
#function


Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’.
The length of the string is variable. The task is to find the minimum number of ‘*’
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

eg:2
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)


# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="mohan", " sai ", " Hari "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("mohan", 'Ussu', 'Alone')


# Eg:2

def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
print("My name is", val,"My age is",age)("mohan",'name2','name3',28) # error ---> age has no args


def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
profile(28,"mohan")

# ? Eg:5
class person:
    fname = "sidhu" #attible or static variable
    lname ="T"

    def frist_name(person):
        print(person.fname)

    def full_name(self):
        print(self.fname+" "+self.lname)
        '''
#1.) Write a Python script to generate and print a dictionary that #contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n=5): # Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
#2.) Find the uncommon words from 2 strings
##s1 "Hello how are you"
#52 "Hello how is"
#3.) Wrire a code print the 8th fihanochi number





