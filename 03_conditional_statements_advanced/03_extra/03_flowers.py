count_chrysanthemum = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()

price_arrangement = 2
price_chrysanthemum = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_roses = 4.10
    price_tulips = 2.5

elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_roses = 4.5
    price_tulips = 4.15

total_count = count_chrysanthemum + count_roses + count_tulips

total_price_chrysanthemum = count_chrysanthemum * price_chrysanthemum
total_price_roses = count_roses * price_roses
total_price_tulips = count_tulips * price_tulips
total_price = total_price_chrysanthemum + total_price_roses + total_price_tulips

if holiday == "Y":
    total_price *= 1.15

if count_tulips > 7 and season == "Spring":
    total_price *= 0.95

if count_roses >= 10 and season == "Winter":
    total_price *= 0.9

if total_count > 20:
    total_price *= 0.8

print(f"{total_price + price_arrangement:.2f}")
