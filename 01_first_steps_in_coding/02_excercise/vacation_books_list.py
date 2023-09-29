book_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_per_book = book_pages // pages_per_hour

hours_per_day = hours_per_book // days_per_book
print(hours_per_day)