total_detergent_ml = int(input()) * 750

counter = 0
detergent_needed = 0
plates = 0
pots = 0

command = input()
while command != "End":
    dishes = int(command)
    if dishes == int(command):
        counter += 1

    if counter % 3 == 0:
        pots += dishes
        detergent_needed += dishes * 15
    else:
        plates += dishes
        detergent_needed += dishes * 5

    if detergent_needed > total_detergent_ml:
        break

    command = input()

diff = abs(total_detergent_ml - detergent_needed)
if detergent_needed <= total_detergent_ml:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
