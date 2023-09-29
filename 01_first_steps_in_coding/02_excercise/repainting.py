sqm_nylon = int(input())
l_paint = int(input())
l_thinner = int(input())
work_hours = int(input())

price_sqm_nylon = (sqm_nylon + 2) * 1.5
price_l_paint = (l_paint + (l_paint * 0.1)) * 14.5
price_l_thinner = l_thinner * 5
price_bags = 0.4

total_material_price = price_sqm_nylon + price_l_paint + price_l_thinner + price_bags
price_work = total_material_price * 0.3 * work_hours

final_price = total_material_price + price_work

print(final_price)