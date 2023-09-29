pens = int(input())
markers = int(input())
cleaner = int(input())
discount_percentage = int(input())

pens_price = pens * 5.8
markers_price = markers * 7.2
cleaner_price = cleaner * 1.2

total_price = pens_price + markers_price + cleaner_price
discount = total_price * discount_percentage / 100

discounted_price = total_price - discount

print(discounted_price)


