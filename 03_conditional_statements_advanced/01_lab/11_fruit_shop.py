fruit = input()
day = input()
quantity = float(input())

price = 0

if fruit == "banana":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.5 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 2.7 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "apple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.2 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 1.25 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "orange":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 0.85 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 0.9 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "grapefruit":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.45 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 1.6 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "kiwi":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.7 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 3.0 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "pineapple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 5.5 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 5.6 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

elif fruit == "grapes":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 3.85 * quantity
        print(f"{price:.2f}")
    elif day == "Saturday" or day == "Sunday":
        price = 4.2 * quantity
        print(f"{price:.2f}")
    else:
        print("error")

else:
    print("error")