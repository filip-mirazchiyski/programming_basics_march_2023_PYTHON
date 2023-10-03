from sys import maxsize

number = 0
min_number = maxsize

while True:
    command = input()

    if command == "Stop":
        break

    current_num = int(command)

    if current_num < min_number:
        min_number = current_num

print(min_number)

