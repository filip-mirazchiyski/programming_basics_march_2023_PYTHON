budget = float(input())
N = int(input())
M = int(input())
P = int(input())

price_N = 250 * N
price_M = M * (0.35 * price_N)
price_P = P *( 0.10 * price_N)
total_price = price_N + price_M + price_P

if N > M:
    total_price *= 0.85

diff = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")