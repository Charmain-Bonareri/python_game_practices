#The input() function is called inside our Python application and prompts the user to pass in an input, which is stored as a string.

print("What is your name?")
name = input()

print("How old are you?")
age = int(input())

print(name)
print(age)

#Here we are prompting the user for their name and age, and storing them in variables. Since age is a number, we used the int() function to convert it to an integer.


print("How are you feeling today?")
feeling = input()

print("What have you learnt today?")
lesson = input()

print("On a scale of one to ten how does learning python feel?")
scale = int(input())

print(feeling)
print(lesson)
print(scale)

#if statements
#An if statement runs only when the condition passed to it evaluates to true.

height = 74
if height > 70:
    print("you are really tall!")

else:
    print("You are really short")

"""
Python uses indents. Indents are just four spaces we give to our application to define blocks of code. 
If we don't indent blocks of our code, we get an IndentationError and our program won't run.

elif
What if we have more than one condition to check for? We can use elif, which will allow us to check for multiple conditions.

"""

height = 68 # inches
if height > 70 :
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")

"""
This is because the if statement only runs if the output evaluates to be True, 
and since our list is empty the condition evaluates to False
    
"""




