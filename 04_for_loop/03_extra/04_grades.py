students = int(input())

excellent = 0
good = 0
average = 0
fail = 0
total_grades = 0

for result in range(students):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
       fail += 1
       total_grades += grade
    elif 3.00 <= grade <= 3.99:
        average += 1
        total_grades += grade
    elif 4.00 <= grade <= 4.99:
        good += 1
        total_grades += grade
    else:
        excellent += 1
        total_grades += grade

average_grade = total_grades /students
percentage_excellent = excellent / students * 100
percentage_good = good / students * 100
percentage_average = average / students * 100
percentage_fail = fail / students * 100

print(f"Top students: {percentage_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_good:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_average:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {average_grade:.2f}")
