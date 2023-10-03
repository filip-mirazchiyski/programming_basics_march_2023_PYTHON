student_name = input()
grades_counter = 0
years_counter = 0
failed_years = 0

while True:
    student_grade = float(input())

    if student_grade < 4:
        failed_years += 1

        if failed_years == 2:
            current_failed_year = years_counter + 1
            print(f"{student_name} has been excluded at {current_failed_year} grade")
            break

        continue


    years_counter += 1
    grades_counter += student_grade

    if years_counter == 12:
        average_grades = grades_counter / years_counter
        print(f"{student_name} graduated. Average grade: {average_grades:.2f}")
        break


