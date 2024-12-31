#Prompt the user to enter two numbers (e.g., num1 and num2). Convert the input to float for more flexibility in calculations.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

#Different operations on the two numbers
add = num1 + num2
print("The sum of the two numbers is: ", add)
div = num1 - num2
print("The difference of the two numbers is: ", div)
product = num1 * num2
print("The product of the two numbers is: ", product)
quotient = num1 / num2
print("The quotient of the two numbers is: ", quotient)
remainder = num1 % num2
print("The remainder of the two numbers is: ", remainder)
raise2p = num1 ** num2
print("The result of raising the first number to the power of the second number is: ", raise2p)
floord = num1 // num2
print("The result of floor division of the two numbers is: ", floord)

#Comparison of the two numbers
if num1 > num2:
    print("The first number is greater than the second number.")
if num1 < num2:
    print("The first number is less than the second number.")
if num1 == num2:
    print("The two numbers are equal.")
if num1 != num2:
    print("The two numbers are not equal.")
    
#Logical Operators
num3 = float(input("Enter a third number: "))
if num3 > num1 and num2:
    print("The third number is the greatest of the three numbers.")
if num3 < num1 and num2:
    print("The third number is the smallest of the three numbers.")
if num1 < num3 < num2:
    print("The third number is between the first and second numbers.")
    
#Assignment Operators
result = num1 + num2
result += 10
print("The result of the assignment operation is: ", result)