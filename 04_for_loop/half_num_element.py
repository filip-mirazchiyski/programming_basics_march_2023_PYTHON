from sys import maxsize

n = int(input())
sum = 0
max_num = -maxsize

for i in range(n):
    current_num = int(input())
    sum += current_num
    if current_num > max_num:
        max_num = current_num

sum -= max_num

if max_num == sum:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum)}")

