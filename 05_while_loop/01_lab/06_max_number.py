from sys import maxsize

number = 0
max_number = -maxsize

while True:
    command = input()

    if command == "Stop":
        break

    current_num = int(command)

    if current_num > max_number:
        max_number = current_num

print(max_number)

