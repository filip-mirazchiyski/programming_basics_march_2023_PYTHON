actor_name = input()
points = float(input())
judges = int(input())

needed_points = 1250.5

for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points / 2

    if points > needed_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

if points <= needed_points:
    print(f"Sorry, {actor_name} you need {needed_points - points:.1f} more!")
    