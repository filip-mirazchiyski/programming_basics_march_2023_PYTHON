w = float(input()) * 100
h = float(input()) * 100
print("%.0f" % w)
print("%.0f" % h)

h1 = h - 100
print("%.0f" % h1)

desks_per_row = h1 // 70
print("%.0f" % desks_per_row)

rows = w // 120
print("%.0f" % rows)

total_desks = desks_per_row * rows - 3
print("%.0f" % total_desks)

