minutes_per_walk = int(input())
walks = int(input())
calorie_intake_per_day = int(input())

total_walk_time = minutes_per_walk * walks

calorie_burn_per_day = total_walk_time * 5

if calorie_burn_per_day >= calorie_intake_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calorie_burn_per_day}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calorie_burn_per_day}.")