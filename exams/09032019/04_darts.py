player = input()
starting_points = 301
shot_count = 0

command = input()

while command != "Retire" or starting_points == 0:
    command = input()
    shot_points = int(input())
    if command == "Single" and shot_points < starting_points:
        shot_count += 1
        starting_points -= shot_points
    elif command == "Double" and shot_points < starting_points:
        shot_count += 1
        starting_points -= shot_points * 2
    elif starting_points == "Triple" and shot_points < starting_points:
        shot_count += 1
        starting_points -= shot_points * 3