groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(groups):
    people = int(input())

    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        montblanc += people
    elif 13 <= people <= 25:
        kilimanjaro += people
    elif 26 <= people <= 40:
        k2 += people
    else:
        everest += people

total = musala + montblanc + kilimanjaro + k2 + everest

percentage_musala = musala / total * 100
percentage_montblanc = montblanc / total * 100
percentage_kilimanjaro = kilimanjaro / total * 100
percentage_k2 = k2 / total * 100
percentage_everest = everest / total * 100

print(f"{percentage_musala:.2f}%")
print(f"{percentage_montblanc:.2f}%")
print(f"{percentage_kilimanjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")