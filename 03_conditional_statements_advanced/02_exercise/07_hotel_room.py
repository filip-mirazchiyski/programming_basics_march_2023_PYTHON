month = input()
nights = int(input())

total_price_studio = 0
total_price_apartment = 0
discount_studio = 1
discount_apartment = 1

if month == "May" or month == "October":
    total_price_studio = 50
    total_price_apartment = 65
    if 7 < nights <= 14:
        discount_studio *=.95
    if nights > 14:
        discount_studio *= .7
        discount_apartment *= .9

elif month == "June" or month == "September":
    total_price_studio = 75.20
    total_price_apartment = 68.70
    if nights > 14:
        discount_studio *= .8
        discount_apartment *= .9

elif month == "July" or month == "August":
    total_price_studio = 76
    total_price_apartment = 77
    if nights > 14:
        discount_apartment *= .9

total_price_studio = (total_price_studio * nights) * discount_studio
total_price_apartment = (total_price_apartment * nights) * discount_apartment

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")