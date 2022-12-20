from datetime import datetime, timedelta

today = datetime.now()

print((today))


color = input("What is your favorite color? ")
if color == "blue":
    print("i like blue too")

    color = input("What is your favorite color?")
if color == "blue":
    print("i like blue too")

color = input("Please enter a color? ")

# This if statement will only match "blue" not "Blue" or "BLUE"
if color == "blue":
    print("I like blue too.")

# This if statement will match the word blue, regardless of the capitalization
if color.lower() == "blue":
    print("I like blue too.")
