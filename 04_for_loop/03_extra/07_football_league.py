stadium_capacity = int(input())
fans = int(input())

fans_team_1_a = 0
fans_team_1_b = 0
fans_team_2_v = 0
fans_team_2_g = 0

for i in range(fans):
    sector = input()
    if sector == "A":
        fans_team_1_a += 1
    elif sector == "B":
        fans_team_1_b += 1
    elif sector == "V":
        fans_team_2_v += 1
    elif sector == "G":
        fans_team_2_g += 1

total_fans = fans_team_1_a + fans_team_1_b + fans_team_2_v + fans_team_2_g
percentage_a = fans_team_1_a / total_fans * 100
percentage_b = fans_team_1_b / total_fans * 100
percentage_v = fans_team_2_v / total_fans * 100
percentage_g = fans_team_2_g / total_fans * 100
percentage_all = total_fans / stadium_capacity * 100

print(f"{percentage_a:.2f}%")
print(f"{percentage_b:.2f}%")
print(f"{percentage_v:.2f}%")
print(f"{percentage_g:.2f}%")
print(f"{percentage_all:.2f}%")


