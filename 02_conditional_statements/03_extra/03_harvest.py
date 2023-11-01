
import math

X = int(input())
Y = float(input())
Z = int(input())
workers = int(input())

total_grape = X * Y
wine_l = (total_grape * 0.4) / 2.5

if wine_l >= Z:
    left_wine = wine_l - Z
    wine_l_per_worker = left_wine / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine_l)} liters.\n{math.ceil(left_wine)} "
          f"liters left -> {math.ceil(wine_l_per_worker)} liters per person.")
else:
    wine_l = abs(wine_l - Z)
    print(f"It will be a tough winter! More {math.floor(wine_l)} liters wine needed.")