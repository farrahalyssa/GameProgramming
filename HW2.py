
print("1) for loop that prints 1 to 10, excluding 11")
for i in range (1,11):
    print(i)
    

print("2) while loop that prints 1 to 10")
count = 1
while (count < 11):
  print(count)
  count += 1

print('3) if statement')
answer = input("what is the color of the sky?").lower()

if (answer == "blue" ):
    print("correct")
# you can also use elif if there's another option
else:
    print("incorrect")

print('4) random number generator')
#generates and prints a random number from 0 to 10
from random import randint
print(randint(0,10))

print('5) shopping list, printing arrays of strings')
# prints an array of strings using a for loop
shoppingCart=["milk", "eggs", "bread", "cheese"]
print("Index 0: " + shoppingCart[0]) #string concatenation
print("Items in the shopping cart:")
for x in shoppingCart:
    print(x)
print("Those are in your shopping cart.")


print('6) simple calculator')
import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} / {num2} = {modulus}")