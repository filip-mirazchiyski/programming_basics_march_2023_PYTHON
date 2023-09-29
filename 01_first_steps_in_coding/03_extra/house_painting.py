x = float(input())
y = float(input())
h = float(input())
xy = x * y
xx = x * x

xyxy = xy * 2 - (2 * 1.5 * 1.5)
xxxx = xx * 2 - 1.2 * 2

xyxy1 = xy * 2
z = x * h /2
zz = z * 2

green = (xyxy + xxxx) / 3.4
red = (xyxy1 + zz) /4.3

print("%.2f" % green)
print("%.2f" % red)