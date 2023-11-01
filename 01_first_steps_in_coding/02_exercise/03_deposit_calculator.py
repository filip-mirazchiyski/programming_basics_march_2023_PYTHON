deposit_sum = float(input())
deposit_duration = int(input())
yearly_interest_percentage = float(input())

final_sum = deposit_sum + deposit_duration * (((deposit_sum * yearly_interest_percentage)/100) / 12)
print(final_sum)
