import random

# Generate the target number once, outside the loop
target = random.randint(1, 100)

while True:
    try:
       number = int(input("Enter a number between 1 and 100: "))
    except ValueError:
        print("enter an integer value")
        continue

    if number == target:
        print(f"Congratulations!! You guessed right! The number is {target}")
        break  # Exit the loop when the guess is correct
    elif number > target:
        print(f"Your number {number} is greater than the target number.")
    else:
        print(f"Your number {number} is less than the target number.")
