budget = float(input())
action = False

while True:
    command = input()

    if command == "ACTION" or budget <= 0:
        break

    actor = command

    if len(actor) <= 15:
        salary = float(input())
    else:
        salary = budget * 0.2

    budget -= salary

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
