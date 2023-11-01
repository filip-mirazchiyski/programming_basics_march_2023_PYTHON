fuel = str(input())
l = float(input())

a = "Diesel"
b = "Gasoline"
c = "Gas"

if l < 25:
    if fuel == a:
        print(f"Fill your tank with {fuel.lower()}!")
    elif fuel == b:
        print(f"Fill your tank with {fuel.lower()}!")
    elif fuel == c:
        print(f"Fill your tank with {fuel.lower()}!")
    else:
        print("Invalid fuel!")
else:
    l >= 25
    if fuel == a:
        print(f"You have enough {fuel.lower()}.")
    elif fuel == b:
        print(f"You have enough {fuel.lower()}.")
    elif fuel == c:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"You have enough {fuel}.")
