chicken = int(input())
fish = int(input())
veg = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.4
veg_price = veg * 8.15

mains = chicken_price + fish_price + veg_price
dessert = mains * 0.2
delivery = 2.5

total_price = mains + dessert + delivery

print(total_price)
