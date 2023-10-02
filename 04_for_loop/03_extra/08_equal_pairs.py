count = int(input())
first_sum = int(input()) + int(input())
max_difference = 0

for i in range(count - 1):
    current_sum = int(input()) + int (input())
    sum = abs(first_sum - current_sum)
    if sum > max_difference:
        max_difference = sum
        first_sum = current_sum

if max_difference == 0:
    print(f"Yes, value={first_sum}")
else:
    print(f"No, maxdiff={max_difference}")