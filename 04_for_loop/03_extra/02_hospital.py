period = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, period + 1):
    current_patients = int(input())

    if day % 3 == 0 and (untreated_patients > treated_patients):
        doctors += 1

    if current_patients <= doctors:
        treated_patients += current_patients
    else:
        treated_patients += doctors
        untreated_patients += current_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

