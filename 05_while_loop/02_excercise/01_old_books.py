favorite_book = input()
current_book = input()

book_counter = 0
is_found = False

while current_book != "No More Books":
    if current_book == favorite_book:
        is_found = True
        break

    book_counter += 1
    current_book = input()

if is_found == False:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")

else:
    print(f"You checked {book_counter} books and found it.")
