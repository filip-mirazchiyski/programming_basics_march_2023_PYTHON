from sys import maxsize

current_player = ""
goals_scored = 0
hat_trick = False
max_goals = -maxsize
best_player_name = ""

player_name = input()

while player_name != "END":
    goals_scored = int(input())
    current_player = player_name

    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player_name = current_player
    if goals_scored >= 10:
        break

    player_name = input()

print(f"{best_player_name} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
