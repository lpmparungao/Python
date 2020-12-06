#Hello World
print("1. Hello World")

print("Hello World!\n")

#Shape
print("2. Shape")

print("   /|")
print("  / |")
print(" /  |")
print("/___|\n")

#Variables
print("3. Variables")

character_name = "John"
character_age = 35
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".\n")

#Strings
print("4. Strings")

#functions
phrase = "I really like you."
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
#length len
print(len(phrase))
#index
print(phrase[2])
print(phrase.index("I"))
#replace
print(phrase.replace("I", "Lance"))

print("")

#Numbers
print("5. Numbers")

print(-2.0987)
print(3 + 5 + 4)
print(315 * 801)
print(10 % 3)
cs_num1 = 5
print(str(cs_num1) + " is my lucky number")
#Absolute Value
cs_num2 = -24
print(abs(cs_num2))
#Power
print(pow(4, 3))
#Higer/Lower
print(max(5, 12))
print(min(5, 12))
#import math functions
from math import *
#Round Off, Round Down, Round Up
print(round(3.5))
print(floor(3.9))
print(ceil(3.1))
print(sqrt(144))

print("")

#Getting Input from Users
print("6. Getting Input")

#cs_input_name = input("Enter your name: ")
#cs_input_age = input("Enter your age: ")
#print("Hello " + cs_input_name + "! You are " + cs_input_age + " years old!")

print("")

#Calculator
print("7. Calculator")

#cs_calc_num1 = input("Enter a number: ")
#cs_calc_num2 = input("Enter another number: ")
#result = float(cs_calc_num1) + float(cs_calc_num2)
#print(result)

print("")

#MadLibs
print("8. Madlibs")

#madlib_color = input("Enter a color: ")
#madlib_noun = input("Enter a plural noun: ")
#madlib_celeb =input("Enter a celebrity: ")
#print("Roses are " + madlib_color)
#print(madlib_noun + " are blue")
#print("I love " + madlib_celeb)

print("")

#Lists
print("9. Lists")
cs_friends_list = ["Chaewon", "Yuri", "Yena", "Hitomi"]
print(cs_friends_list[0])
print(cs_friends_list[-1])
#start to onwards
print(cs_friends_list[1:])
#start and end
print(cs_friends_list[0:3])
#modify/update
cs_friends_list[3] = "Yujin"
print(cs_friends_list[3])

print("")

#List Functions
print("10. List Functions")
cs_lf_numbers = [10, 29, 18, 8, 1]
cs_lf_friends = ["Chaewon","Yena", "Yuri", "Yujin", "Eunbi"]
print(cs_lf_friends)
#add other list
cs_lf_friends.extend(cs_lf_numbers)
print(cs_lf_friends)
#add item
cs_lf_friends = ["Chaewon","Yena", "Yuri", "Yujin", "Eunbi"]
cs_lf_friends.append("Minju") #at end
cs_lf_friends.insert(4, "Hitomi")
print(cs_lf_friends)
#remove item
cs_lf_friends.remove("Hitomi")
print(cs_lf_friends)
#remove last item
#cs_lf_friends.pop()
cs_lf_numbers.sort()
print(cs_lf_numbers)
cs_lf_numbers.reverse()
print(cs_lf_numbers)
cs_lf_izone = cs_lf_friends.copy()
cs_lf_izone.extend(["Hitomi", "Chaeyeon", "Nako", "Sakura", "Wonyoung", "Hyewon"])
print(cs_lf_izone)

print("")

#Tuples can't modify
print("11. Tuples")

cs_tuples_numbers = (3 , 4 , 5 , 6 , 7)
print(cs_tuples_numbers[4])
cs_listoftuples = [(1,2), (3,4)]
print(cs_listoftuples[1])

print("")

#Functions
print("12. Functions")

def say_hi():
    print("Hi")
say_hi()
def hi_user(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
hi_user("Chaewon", 20)

print("")

#Return
print("13. Return")

def ret_cube(ret_num):
    return ret_num * ret_num * ret_num
ret_result = ret_cube(4)
print(ret_result)

print("")

#If statements
print("14. If Statements")

if_hungry = True
if_thereisfood= False

if if_hungry and if_thereisfood:
    print("I ate breakfast")
else:
    print("I skipped breakfast")

if_ismale = False
if_istall = False

if if_ismale and if_istall:
    print("You are a tall male")
elif if_ismale and not(if_istall):
    print("You are a short male")
elif not(if_ismale) and if_istall:
    print("You are a tall female")
else:
    print("You are a short female")

print("")

#If statements + comparisons
print("15. If statements + comparisons")

def compare_maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
compare_result = compare_maxnum(3, 4, 5)
print(compare_result)

print("")

#Calculator2
print("16, Calculator 2")

#cal2_num1 = float(input("Enter a number: "))
#cal2_op = input("Enter operator: ")
#cal2_num2 = float(input("Enter the second number: "))

#if cal2_op == "+":
    #print(cal2_num1 + cal2_num2)
#elif cal2_op == "-":
   # print(cal2_num1 - cal2_num2)
#elif cal2_op == "*":
   # print(cal2_num1 * cal2_num2)
#elif cal2_op == "/":
   # print(cal2_num1 / cal2_num2)
#else:
    #print("Invalid operator")

print("")

#Dictionaries
print("17. Dictionaries")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Jan"])
print(monthConversions["Mar"])
print(monthConversions.get("Feeb", "Invalid key"))

print("")

#While Loop
print("18. While Loop")

while_num1 = 1
while while_num1 <= 5:
    print(while_num1)
    while_num1 += 1

print("")

#Guessing Game
print("19. Guessing Game")

#gg_word = "Chaewon"
#gg_guess = ""
#gg_guess_count = 0
#gg_guess_limit =  3
#gg_outofguess = False
#while gg_guess != gg_word and not gg_outofguess:
    #if gg_guess_count < gg_guess_limit:
        #gg_guess = input("Enter your guess: ")
        #gg_guess_count += 1
    #else:
        #gg_outofguess = True
#if gg_guess == gg_word:
    #print("You win! Congratulations!")
#else:
    #print("Out of guesses :<")

print("")

#For Loop
print("20. For loop")
for_joyuriz = ["Chaewon", "Yena", "Yuri"]
for member in for_joyuriz:
    print(member)
for mem_index in range(len(for_joyuriz)):
    print(for_joyuriz[mem_index])
for index in range(5, 10):
    print(index)

print("")

#Exponent Function
print("21. Exponent Function")
print(2**3)
def exponent(base_num, pow_num):
    result = 1
    for index in range (pow_num):
        result = result * base_num
    return result
print(exponent(3, 5))

print("")

#2D Lists
print("22. 2D Lists")
twoD_list =[
    [1, 2, 3],
    [4, 5 ,6],
    [7, 8, 9],
    [0]
    ]

print(twoD_list[2][2])

print("")

#Nested for loops
print("23. Nested For loops")
two_dimensional =[
    [1, 2, 3],
    [4, 5 ,6],
    [7, 8, 9],
    [0]
    ]

for row in twoD_list:
    for col in row:
        print(col)

print("")

#Translator
print("24. Translator")
#vowels -> c

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            if letter.isupper():
                translation = translation + "C"
            else:
                translation = translation + "c"
        else:
            translation = translation + letter
    return translation
print(translate("Chaewon"))

print("")

#Try Except
print("25. Try Except/Errors")

#try:
    #10/0
    #number = int(input("Enter a number: "))
    #print(number)
#except ZeroDivisionError as err:
  # print(err)
#except ValueError:
    #print("Invalid Input")

print("")

#Reading Files
print("26. Reading Files")
# r read w write a append r+ read&write
employee_file = open("employees.txt", "r")
#print(employee_file.readlines()[1])
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

print("")

#Writing to Files
print("27. Writing to Files")
employees_file = open("employees.txt", "a")
employees_file.write("\nToby - Human Resources")
employees_file.close()

print("")

#Modules and Pip
print("28. Modules and Pip")
#from tools.py
import tools
print(tools.roll_dice(6))

print("")

#Classes and Objects
print("29. Classes and Objects")
#student.py class
#creating student
from student import Student

student1 = Student("Chaewon", 20, False, "Music")
student2 = Student("Yena", 21, False, "Music")
print(student1.name + " " + str(student1.age))
print(student2.name + " " + str(student2.age))

print("")

#Multiple Choice Quiz
print("30. Multiple Choice Quiz")
'''
#import Questions.py
from Question import Question
question_prompts = [
    "What is Chaewon's Color?\n(a) Mint Green\n(b) Mint Blue\n(c) Purple\n",
    "\nWhat is Yena's Color?\n(a) Orange\n(b) White\n(c) Yellow\n",
    "\nWhat is Yuri's Color?\n(a) Pink\n(b) Orange\n(c) Coral\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score))

run_test(questions)
'''
print("")

#Object Functions
print("31. Object Functions")
from student import Student
student3 = Student("Yuri", 19, False, "Music")
student4 = Student("Yujin", 17, False, "Music")
print(student3.legal_age())

print("")

#Inheritance
print("32. Inheritance")
from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_specialdish()

my_chinesechef = ChineseChef()
my_chinesechef.make_specialdish()