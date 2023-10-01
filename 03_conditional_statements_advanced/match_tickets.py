budget = float(input())
category = input()
people = int(input())

transport = 0
diff = 0
ticket_count = 0

vip_total_price = people * 499.99
normal_total_price = people * 249.99
remainder = 0

if category == "VIP":
    if 1 <= people <= 4:
        transport = budget * 0.75
        diff = abs(budget - transport)
        remainder = diff - vip_total_price
    elif 5 <= people <= 9:
        transport = budget * 0.60
        diff = abs(budget - transport)
        remainder = diff - vip_total_price
    elif 10 <= people <= 24:
        transport = budget * 0.5
        diff = abs(budget - transport)
        remainder = diff - vip_total_price
    elif 25 <= people <= 49:
        transport = budget * 0.4
        diff = abs(budget - transport)
        remainder = diff - vip_total_price
    else:
        transport = budget * 0.25
        diff = abs(budget - transport)
        remainder = diff - vip_total_price

if category == "Normal":
    if 1 <= people <= 4:
        transport = budget * 0.75
        diff = abs(budget - transport)
        remainder = diff - normal_total_price
    elif 5 <= people <= 9:
        transport = budget * 0.60
        diff = abs(budget - transport)
        remainder = diff - normal_total_price
    elif 10 <= people <= 24:
        transport = budget * 0.5
        diff = abs(budget - transport)
        remainder = diff - normal_total_price
    elif 25 <= people <= 49:
        transport = budget * 0.4
        diff = abs(budget - transport)
        remainder = diff - normal_total_price
    else:
        transport = budget * 0.25
        diff = abs(budget - transport)
        remainder = diff - normal_total_price

if diff > vip_total_price and category == "VIP":
    print(f"Yes! You have {abs(remainder):.2f} leva left.")
elif diff < vip_total_price and category == "VIP":
    print(f"Not enough money! You need {abs(remainder):.2f} leva.")
elif diff > normal_total_price and category == "Normal":
    print(f"Yes! You have {abs(remainder):.2f} leva left.")
elif diff < normal_total_price and category == "Normal":
    print(f"Not enough money! You need {abs(remainder):.2f} leva.")

