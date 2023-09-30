trip_price = float(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

puzzle = 2.6
doll = 3.0
teddy = 4.1
minion = 8.2
truck = 2.0
discount = 0

sum_puzzle = puzzle * a
sum_doll = doll * b
sum_teddy = teddy * c
sum_minion = minion * d
sum_truck = truck * e
sum_total = sum_puzzle + sum_doll + sum_teddy + sum_minion + sum_truck

total_items = a + b + c + d + e

if total_items >= 50:
    sum_total = sum_total * 0.75

rent = sum_total * 0.1

profit = sum_total - rent
diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
