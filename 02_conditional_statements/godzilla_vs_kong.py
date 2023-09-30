budget = float(input())
extras = int(input())
costumes_price_per_extra = float(input())

set_price = budget * 0.1
costumes_price = costumes_price_per_extra * extras

if extras > 150:
    costumes_price *= 0.9

total_price = set_price + costumes_price
diff = abs(budget - total_price)

if budget >= total_price:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
