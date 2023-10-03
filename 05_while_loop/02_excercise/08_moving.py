space_width = int(input())
space_lenght = int(input())
space_height = int(input())

volume = space_width * space_lenght * space_height

while volume > 0:
    command = input()
    if command == "Done":
        break
    volume -= int(command)

if volume > 0:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
