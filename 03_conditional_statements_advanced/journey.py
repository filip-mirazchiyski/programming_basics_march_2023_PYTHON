budget = float(input())
season = input()

destination = ""
place = "Hotel"
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        place = "Camp"
    elif season == "winter":
        price = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        place = "Camp"
    elif season == "winter":
        price = budget * 0.8

else:
    budget > 1000
    destination = "Europe"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")
