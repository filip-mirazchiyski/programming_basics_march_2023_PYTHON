dancers = int(input())
points = float(input())
season = input()
location = input()

award = 0

if location == "Bulgaria" and season == "summer":
    award = (dancers * points) * 0.95
elif location == "Bulgaria" and season == "winter":
    award = (dancers * points) * 0.92
elif location == "Abroad" and season == "summer":
    award = (dancers * points * 1.5) * 0.90
elif location == "Abroad" and season == "winter":
    award = (dancers * points * 1.5) * 0.85

donation = award * 0.75
remaining_award = award - donation
award_pp = remaining_award / dancers

print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {award_pp:.2f}")
