n = int(input())

total_rakia = 0
total_degrees = 0

for days in range(1, n + 1):
    rakia_l = float(input())
    rakia_degrees = float(input()) * rakia_l
    total_rakia += rakia_l
    total_degrees += rakia_degrees

degrees_per_liter = total_degrees / total_rakia

print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {degrees_per_liter:.2f}")

if degrees_per_liter < 38:
    print("Not good, you should baking!")
elif 38 <= degrees_per_liter <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")


