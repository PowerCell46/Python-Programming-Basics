number_of_the_jury = int(input())
sum_of_grades_1 = 0
counter = 0
while True:
    number_of_the_jury_1 = number_of_the_jury
    name_of_the_presentation = str(input())
    if name_of_the_presentation == "Finish":
        break
    sum_of_grades = 0
    while number_of_the_jury_1 > 0:
        current_grade = float(input())
        sum_of_grades += current_grade
        number_of_the_jury_1 -= 1
    average_grade = sum_of_grades / number_of_the_jury
    sum_of_grades_1 += average_grade
    counter += 1
    print(f'{name_of_the_presentation} - {average_grade:.2f}.')

final_grade = sum_of_grades_1 / counter
print("Student's final assessment is " + (f'{final_grade:.2f}.'))
