jersey_price = float(input())
needed_sum = float(input())

shorts_price = jersey_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (jersey_price + shorts_price) * 2

bill = (jersey_price + shorts_price + socks_price + shoes_price) * 0.85

diff = abs(needed_sum - bill)

if bill >= needed_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {bill:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
