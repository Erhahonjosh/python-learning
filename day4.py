print("Day 4 is running")
# 1. While loop basics
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1

# 2. Password checker
password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted ✅")   

# 3. Mini Game: Guess the Number
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret_number:
        print("Too low ❌")
    elif guess > secret_number:
        print("Too high ❌")
    else:
        print("Correct! 🎉")
