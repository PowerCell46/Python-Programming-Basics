student_counter = 0
standard_counter = 0
kid_counter = 0
all_counter = 0
finish_is_used = False

while True:
    movie_name = str(input())

    if movie_name == "Finish":
        finish_is_used == True
        break

    number_of_free_seats = int(input())
    sum_of_taken_seats = 0
    while True:
        type_of_ticket = str(input())
        if sum_of_taken_seats == number_of_free_seats or type_of_ticket == "End":
            break
        sum_of_taken_seats += 1
        all_counter += 1
        if type_of_ticket == "student":
            student_counter += 1
        elif type_of_ticket == "standard":
            standard_counter += 1
        elif type_of_ticket == "kid":
            kid_counter += 1
    percentage = sum_of_taken_seats / (number_of_free_seats / 100)
    print(f'{movie_name} - {percentage:.2f}% full.')

if finish_is_used == True:
    student_percentage = student_counter / (all_counter / 100)
    standard_percentage = standard_counter / (all_counter / 100)
    kid_percentage = kid_counter / (all_counter / 100)
    print(f'Total tickets: {all_counter}')
    print(f'{student_percentage:.2f}% student tickets.')
    print(f'{standard_percentage:.2f}% standard tickets.')
    print(f'{kid_percentage:.2f}% kids tickets.')