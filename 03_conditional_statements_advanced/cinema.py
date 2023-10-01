type = input()
rows = int(input())
columns = int(input())

price = 0

if type == "Premiere":
    price = 12 * rows * columns
    print(f"{price:.2f} leva")

elif type == "Normal":
    price = 7.50 * rows * columns
    print(f"{price:.2f} leva")

elif type == "Discount":
    price = 5 * rows * columns
    print(f"{price:.2f} leva")