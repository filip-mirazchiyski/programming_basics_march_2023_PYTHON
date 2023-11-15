budget = float(input())
season = input()

car = ""
car_type = ""

if budget <= 100 and season == "Summer":
    car = "Cabrio"
    car_type = "Economy class"
    budget *= 0.35

elif budget <= 100 and season == "Winter":
    car = "Jeep"
    car_type = "Economy class"
    budget *= 0.65

elif 100 <= budget <= 500 and season == "Summer":
    car = "Cabrio"
    car_type = "Compact class"
    budget *= 0.45

elif 100 <= budget <= 500 and season == "Winter":
    car = "Jeep"
    car_type = "Compact class"
    budget *= 0.8

elif budget > 500 and season == "Summer":
    car = "Jeep"
    car_type = "Luxury class"
    budget *= 0.9

elif budget > 500 and season == "Winter":
    car = "Jeep"
    car_type = "Luxury class"
    budget *= 0.9

print(car_type)
print(f"{car} - {budget:.2f}")
