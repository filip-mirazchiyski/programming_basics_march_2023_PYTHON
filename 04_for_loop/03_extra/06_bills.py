months = int(input())

electricity = 0
water = 0
internet = 0


for i in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15

others = (electricity + water + internet) * 1.2
total_bills = electricity + water + internet + others
average_bills = total_bills / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_bills:.2f} lv")
