
num1 = input("Insert a number:")
variable = input ("Insert a variable(+,-,*,/):")
num2 = input("Insert a number:")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if variable == "+":
    print(add)

elif variable == "-":
    print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)

else:
    print("Error: Invalid input")
