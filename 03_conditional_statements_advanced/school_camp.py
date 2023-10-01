season = input()
group = input()
count_students = int(input())
count_nights = int(input())

sport = ""
price_per_night = 0

if season == "Winter" and group == "boys":
    price_per_night = 9.6
    sport = "Judo"
elif season == "Winter" and group == "girls":
    price_per_night = 9.6
    sport = "Gymnastics"
elif season == "Winter" and group == "mixed":
    price_per_night = 10
    sport = "Ski"

if season == "Spring" and group == "boys":
    price_per_night = 7.2
    sport = "Tennis"
elif season == "Spring" and group == "girls":
    price_per_night = 7.2
    sport = "Athletics"
elif season == "Spring" and group == "mixed":
    price_per_night = 9.5
    sport = "Cycling"

if season == "Summer" and group == "boys":
    price_per_night = 15
    sport = "Football"
elif season == "Summer" and group == "girls":
    price_per_night = 15
    sport = "Volleyball"
elif season == "Summer" and group == "mixed":
    price_per_night = 20
    sport = "Swimming"

total_price = count_students * price_per_night * count_nights

if count_students >= 50:
    total_price *= 0.5
elif 50 > count_students >= 20:
    total_price *= 0.85
elif 20 > count_students >= 10:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")