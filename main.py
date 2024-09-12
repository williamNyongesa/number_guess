import random
target = random.randint(1,100)

while True:
    number = int(input("enter a number between 1 and 100 :"))

    if number == target:
        print( f"Congratulations!! you guessed right, The number is {target}")
        break
    if number > target:
        print(f"number {number} is greater that target number")
    elif number < target:
        print(f"number {number} is less that target number")
