days = int(input())
type_room = input()
feedback = input()


total_price_room_for_one_person = 18 * (days - 1)
total_price_apartment = 25 * (days - 1)
total_price_president_apartment = 35 * (days - 1)

if type_room == "room for one person":
    if feedback == "positive":
        total_price_room_for_one_person *= 1.25
    elif feedback == "negative":
        total_price_room_for_one_person *= 0.9
    print(f"{total_price_room_for_one_person:.2f}")

if type_room == "apartment":
    if days < 10:
        if feedback == "positive":
            total_price_apartment *= .7 * 1.25
        elif feedback == "negative":
            total_price_apartment *= .7 * 0.9
    elif 10 <= days <= 15:
        if feedback == "positive":
            total_price_apartment *= .65 * 1.25
        elif feedback == "negative":
            total_price_apartment *= .65 * 0.9
    elif days > 15:
        if feedback == "positive":
            total_price_apartment *= .5 * 1.25
        elif feedback == "negative":
            total_price_apartment *= .5 * 0.9
    print(f"{total_price_apartment:.2f}")

elif type_room == "president apartment":
    if days < 10:
        if feedback == "positive":
            total_price_president_apartment *= .9 * 1.25
        elif feedback == "negative":
            total_price_president_apartment *= .9 * 0.9
    elif 10 <= days <= 15:
        if feedback == "positive":
            total_price_president_apartment *= .85 * 1.25
        elif feedback == "negative":
            total_price_president_apartment *= .85 * 0.9
    elif days > 15:
        if feedback == "positive":
            total_price_president_apartment *= .8 * 1.25
        elif feedback == "negative":
            total_price_president_apartment *= .8 * 0.9
    print(f"{total_price_president_apartment:.2f}")
