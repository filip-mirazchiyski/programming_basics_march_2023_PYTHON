from math import floor
from math import ceil

days = int(input())
total_kg_left = int(input())
dog_kg_per_day = float(input())
cat_kg_per_day = float(input())
turtle_g_per_day = float(input())

total_dog = days * dog_kg_per_day
total_cat = days * cat_kg_per_day
total_turtle = days * turtle_g_per_day / 1000
total_kg_eaten = total_dog + total_cat + total_turtle
diff = abs(total_kg_left - total_kg_eaten)

if total_kg_left > total_kg_eaten:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
