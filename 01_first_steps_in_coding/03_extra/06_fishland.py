mackerel_price = float(input())
spratt_price = float(input())
kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_mussles = float(input())

bonito_price = mackerel_price * 1.6
horse_mackerel_price = spratt_price * 1.8
mussels_price = 7.5

bonito_total = bonito_price * kg_bonito
horse_mackerel_total = horse_mackerel_price * kg_horse_mackerel
mussels_total = mussels_price * kg_mussles

total = bonito_total + horse_mackerel_total + mussels_total
print("%.2f" %total)
