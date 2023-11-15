tournaments_count = int(input())
points = int(input())

tournaments_points = 0
tournaments_won = 0

for tournament in range(tournaments_count):
    tournament_stage = input()

    if tournament_stage == "W":
        tournaments_points += 2000
        tournaments_won += 1
    elif tournament_stage == "F":
        tournaments_points += 1200
    elif tournament_stage == "SF":
        tournaments_points += 720

points += tournaments_points
average_points = tournaments_points // tournaments_count
average_tournaments_won = tournaments_won / tournaments_count * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{average_tournaments_won:.2f}%")
