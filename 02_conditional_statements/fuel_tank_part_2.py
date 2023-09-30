fuel = str(input())
l = float(input())
card = str(input())
price = 0

if fuel == "Diesel":
    price = 2.33
    if card == "Yes":
        price -= 12

elif fuel == "Gasoline":
    price = 2.22
    if card == "Yes":
        price -= 0.18

elif fuel == "Gas":
    price = 0.93
    if card == "Yes":
        price -= 0.08

total = l * price

if 20 <= l <= 25:
     total *= 0.92
elif l > 25:
    total *= 0.90

print(f"{total:.2f} lv.")