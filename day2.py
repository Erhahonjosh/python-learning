# 1. User Input & Greeting
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old!")

# 2. Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# 3. Loops
for i in range(1, 6):
    print(f"Counting: {i}")