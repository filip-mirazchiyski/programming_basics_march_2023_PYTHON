from math import ceil

tv_show = (input())
tv_show_time = int(input())
lunchbreak = int(input())

lunch = lunchbreak / 8
relax = lunchbreak / 4
remaining = (lunchbreak - lunch - relax)
diff = ceil(abs(tv_show_time - remaining))

if remaining >= tv_show_time:
    print(f"You have enough time to watch {tv_show} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {diff} more minutes.")
