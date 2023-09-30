km = int(input())
time = (input())
price = 0

taxi_start = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus = 0.09
train = 0.06
a = "day"
b = "night"

if km < 20 and time == a:
    price_taxi = taxi_start + km * taxi_day
    print(f"{price_taxi:.2f}")
elif km < 20 and time == b:
    price_taxi = taxi_start + km * taxi_night
    print(f"{price_taxi:.2f}")
elif 20 <= km < 100:
    price_bus = km * bus
    print(f"{price_bus:.2f}")
else:
    price_train = km * train
    print(f"{price_train:.2f}")
