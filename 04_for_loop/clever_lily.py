age = int(input())
price_wm = float(input())
price_toy = int(input())

money = 0
money_for_year = 10
count_toys = 0
odd_birthdays = 0
even_birthdays = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money += money_for_year
        money -= 1
        money_for_year += 10
    else:
        money += price_toy

diff = abs(money - price_wm)

if money >= price_wm:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")