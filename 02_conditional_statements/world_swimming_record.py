from math import floor

record_sec = float(input())
distance_m = float(input())
sec_per_m = float(input())

result = distance_m * sec_per_m
slowing_down = floor(distance_m / 15) * 12.5

total_time = result + slowing_down
diff = abs(total_time - record_sec)

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
