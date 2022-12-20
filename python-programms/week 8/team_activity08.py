word = "commitment"
favourite = input("What is your favourite letter? ").lower()

for letter in word:
    if letter == favourite:
        print("_", end=" ")
    else:
        print(letter.lower(), end=" ")

#stretch challenge
quote = "in coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

answer = "yes"

while answer.lower() == "yes":
    number = int(input("Give me a number: "))

    for i, letter in enumerate(quote):
        if (i + 1) % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
        print()
        answer = input("Would you like to enter another number? ")


    print("Goodbye!")
