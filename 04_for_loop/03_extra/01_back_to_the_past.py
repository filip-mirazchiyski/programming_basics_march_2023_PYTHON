inheritance = float(input())
final_year = int(input())

age = 17
expenses = 0

for year in range(1800, final_year + 1):
    age += 1

    if year % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + 50 * age

diff = abs(inheritance - expenses)
if inheritance >= expenses:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
