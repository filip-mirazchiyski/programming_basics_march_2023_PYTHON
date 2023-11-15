season = input()
distance = float(input())

km_price = 0

if distance <= 5000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.75
    elif season == "Summer":
        km_price = 0.90
    elif season == "Winter":
        km_price = 1.05
elif 5000 < distance <= 10000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.95
    elif season == "Summer":
        km_price = 1.1
    elif season == "Winter":
        km_price = 1.25
elif 10000 < distance <= 20000:
        km_price = 1.45

gross_income = distance * km_price
net_income = gross_income * 0.9
total_net_income = 4 * net_income

print(f"{total_net_income:.2f}")