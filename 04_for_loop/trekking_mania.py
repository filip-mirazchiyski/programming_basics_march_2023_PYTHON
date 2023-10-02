groups = int(input())

musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for group in range(groups):
    current_number = int(input())
    if current_number <= 5:
        musala_count += current_number
    elif current_number <= 12:
        montblanc_count += current_number
    elif current_number <= 25:
        kilimanjaro_count += current_number
    elif current_number <= 40:
        k2_count += current_number
    else:
        everest_count += current_number

total_count = musala_count + montblanc_count + kilimanjaro_count + k2_count + everest_count
musala_percent = musala_count / total_count * 100
montblanc_percent = montblanc_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
