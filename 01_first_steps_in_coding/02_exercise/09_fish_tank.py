length = int(input())
width = int(input())
height = int(input())
percentage_others = float(input()) / 100

volume_cm = length * width * height
volume_l = volume_cm / 1000

water_percentage = 1 - percentage_others
water_needed = volume_l * water_percentage

print(water_needed)

