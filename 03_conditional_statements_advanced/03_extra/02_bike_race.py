junior_count = int(input())
senior_count = int(input())
race = input()

total_price_junior = 0
total_price_senior = 0
total_price = 0

if race == "trail":
    total_price_junior = junior_count * 5.5
    total_price_senior = senior_count * 7
    total_price = total_price_junior + total_price_senior

elif race == "cross-country":
    total_price_junior = junior_count * 8
    total_price_senior = senior_count * 9.5
    total_price = total_price_junior + total_price_senior
    if 50 <= (junior_count + senior_count):
        total_price *= .75
elif race == "downhill":
    total_price_junior = junior_count * 12.25
    total_price_senior = senior_count * 13.75
    total_price = total_price_junior + total_price_senior

elif race == "road":
    total_price_junior = junior_count * 20
    total_price_senior = senior_count * 21.50
    total_price = total_price_junior + total_price_senior

expenses = total_price * 0.05
diff = total_price - expenses

print(f"{diff:.2f}")
