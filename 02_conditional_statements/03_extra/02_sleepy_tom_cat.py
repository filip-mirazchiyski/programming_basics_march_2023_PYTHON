days_off = int(input())

working_days = 365 - days_off
play_time_days_off = days_off * 127
play_time_working_days = working_days * 63
total_play_time = play_time_days_off + play_time_working_days
diff = abs(30000 - total_play_time)
diff_h = diff // 60
diff_m = diff % 60

if total_play_time > 30000:
    print("Tom will run away")
    print(f"{diff_h} hours and {diff_m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{diff_h} hours and {diff_m} minutes less for play")
