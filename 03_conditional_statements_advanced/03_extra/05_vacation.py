budget = float(input())
season = input()

location = ""
accomodation = ""

if budget <= 1000 and season == "Summer":
    location = "Alaska"
    accomodation = "Camp"
    budget *= 0.65

elif budget <= 1000 and season == "Winter":
    location = "Morocco"
    accomodation = "Camp"
    budget *= 0.45

elif 1000 <= budget <= 3000 and season == "Summer":
    location = "Alaska"
    accomodation = "Hut"
    budget *= 0.8

elif 1000 <= budget <= 3000 and season == "Winter":
    location = "Morocco"
    accomodation = "Hut"
    budget *= 0.6

elif budget > 3000 and season == "Summer":
    location = "Alaska"
    accomodation = "Hotel"
    budget *= 0.9

elif budget > 3000 and season == "Winter":
    location = "Morocco"
    accomodation = "Hotel"
    budget *= 0.9

print(f"{location} - {accomodation} - {budget:.2f}")
