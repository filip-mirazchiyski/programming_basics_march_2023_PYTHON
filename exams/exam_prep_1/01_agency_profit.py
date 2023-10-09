airline_company = input()
adult_tickets = int(input())
child_tickets = int(input())
price_adult_ticket = float(input())
service_tax = float(input())

price_child_ticket = price_adult_ticket * 0.3

final_price_adult = price_adult_ticket + service_tax
final_price_child = price_child_ticket + service_tax

total_price_adult = final_price_adult * adult_tickets
total_price_child = final_price_child * child_tickets

profit = (total_price_adult + total_price_child) * 0.2

print(f"The profit of your agency from {airline_company} tickets is {profit:.2f} lv.")

