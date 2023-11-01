from math import ceil
from math import floor

magnolia = int(input()) * 3.25
hyacinth = int(input()) * 4
rose = int(input()) * 3.50
cactus = int(input()) * 8
gift_price = float(input())

total = (magnolia + hyacinth + rose + cactus) * 0.95
diff = abs(round(gift_price - total,2))

if total > gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
