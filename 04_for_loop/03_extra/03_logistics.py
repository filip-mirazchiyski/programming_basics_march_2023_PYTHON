loads = int(input())

tonnage_per_microbus = 0
tonnage_per_truck = 0
tonnage_per_train = 0

for i in range(loads):
    tonnage = int(input())

    if tonnage <= 3:
        tonnage_per_microbus += tonnage
    elif tonnage <= 11:
        tonnage_per_truck += tonnage
    else:
        tonnage_per_train += tonnage

price_microbus = tonnage_per_microbus * 200
price_truck = tonnage_per_truck * 175
price_train = tonnage_per_train * 120

total_tonnage = tonnage_per_microbus + tonnage_per_truck + tonnage_per_train
total_price = price_microbus + price_truck + price_train
average_tonnage_price = total_price / total_tonnage

percentage_microbus = tonnage_per_microbus / total_tonnage * 100
percentage_truck = tonnage_per_truck / total_tonnage * 100
percentage_train = tonnage_per_train / total_tonnage * 100

print(f"{average_tonnage_price:.2f}")
print(f"{percentage_microbus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")
