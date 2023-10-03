cake_size_a = int(input())
cake_size_b = int(input())

total_cake_size = cake_size_a * cake_size_b

while total_cake_size > 0:
    command = input()
    if command == "STOP":
        print(f"{total_cake_size} pieces are left.")
        break
    total_cake_size -= int(command)

if total_cake_size <= 0:
    print(f"No more cake left! You need {abs(total_cake_size)} pieces more.")
