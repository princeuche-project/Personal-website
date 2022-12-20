with open("books.txt") as book_of_mormon:
    for books in book_of_mormon:
        book = books.strip()
        print(book)
