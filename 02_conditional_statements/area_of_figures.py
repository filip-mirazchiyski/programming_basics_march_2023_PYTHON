from math import pi

figure = (input())
area = 0
if figure == "square":
    sq_lenght = float(input())
    area = sq_lenght * sq_lenght

elif figure == "rectangle":
    rec_lenght = float(input())
    rec_width = float(input())
    area = rec_lenght * rec_width

elif figure == "circle":
    cir_radius = float(input())
    area = (cir_radius ** 2) * pi

elif figure == "triangle":
    tri_lenght = float(input())
    tri_height = float(input())
    area = 0.5 * (tri_lenght * tri_height)

print(f'{area:.3f}')
