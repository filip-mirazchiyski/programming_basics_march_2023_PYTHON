friends_count = int(input())
nights_pp = int(input())
transport_cards_pp = int(input())
museum_tickets_pp = int(input())

night = 20
transport_card = 1.60
museum_ticket = 6

total_nights_pp = nights_pp * night * 1.25 * friends_count
total_transport_cards = transport_cards_pp * transport_card * 1.25 * friends_count
total_museum_tickets = museum_tickets_pp * museum_ticket * 1.25 * friends_count

total = total_nights_pp + total_transport_cards + total_museum_tickets

print(f"{total:.2f}")
