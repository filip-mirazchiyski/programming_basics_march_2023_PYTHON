sq_m_for_landscaping = float(input())
full_price = sq_m_for_landscaping * 7.61
discount = full_price * 0.18
final_price = full_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")