turns = int(input())

points = 0
num_0_9 = 0
num_10_19 = 0
num_20_29 = 0
num_30_39 = 0
num_40_50 = 0
num_invalid = 0




for i in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        num_0_9 +=1
    elif 10 <= number <= 19:
        points += number * 0.3
        num_10_19 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        num_20_29 += 1
    elif 30 <= number <= 39:
        points += 50
        num_30_39 += 1
    elif 40 <= number <= 50:
        points += 100
        num_40_50 += 1
    else:
        points /= 2
        num_invalid += 1

total_num = num_0_9 + num_10_19 + num_20_29 + num_30_39 + num_40_50 + num_invalid
percentage_num_0_9 = num_0_9 / total_num * 100
percentage_num_10_19 = num_10_19 / total_num * 100
percentage_num_20_29 = num_20_29 / total_num * 100
percentage_num_30_39 = num_30_39 / total_num * 100
percentage_num_40_50 = num_40_50 / total_num * 100
percentage_num_invalid = num_invalid / total_num * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percentage_num_0_9:.2f}%")
print(f"From 10 to 19: {percentage_num_10_19:.2f}%")
print(f"From 20 to 29: {percentage_num_20_29:.2f}%")
print(f"From 30 to 39: {percentage_num_30_39:.2f}%")
print(f"From 40 to 50: {percentage_num_40_50:.2f}%")
print(f"Invalid numbers: {percentage_num_invalid:.2f}%")
