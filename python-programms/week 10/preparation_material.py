#ACCESSING ITEMS IN A LIST VIA THEIR INDEX
first = [0]
second = [1]

index = int(input('Which index would you like to get?'))
user_choice = [index]
print(user_choice)


#ITERATING THROUGH A LIST USING AN INDEX

books = 'book'
number_of_books = len(books)
for i in range(len(books)):
    book = books[i]
    print(book, i ) # print each book to the screen.

#WORKING WITH PARALLEL LISTS

names = ['uchenna', 'emeka']
numbers = [12334214, 234543]

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")

