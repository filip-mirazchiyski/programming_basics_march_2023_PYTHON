points = int(input())
bonus = 0
bonus_1 = 0
bonus_2 = 0

if points <= 100:
    bonus = 5
elif 1000 > points > 100:
    bonus = points * 0.2
else:
    bonus = points * 0.1

if points % 2 == 0:
    bonus_1 = 1

if points % 10 == 5:
    bonus_2 = 2

total_bonus = bonus + bonus_1 + bonus_2
total_points = points + + bonus + bonus_1 + bonus_2
print(total_bonus)
print(total_points)
