input_number = int(input())

if input_number < 3:
    print("Invalid number")
else:
    actual_number = input_number - 2

    upper_row_odd = "\ /"
    upper_row_even = "\ /"
    lower_row_odd = "/ \*"
    lower_row_even = "/ \-"

    for i in range(0, 2):
        counter = actual_number
        if i % 2 != 0:
            upper_row_odd = (actual_number * "*") + upper_row_odd + (actual_number * "*")
            upper_row_even = (actual_number * "-") + upper_row_even + (actual_number * "-")
        elif i % 2 == 0:
            lower_row_odd = (actual_number * "*") + lower_row_odd + ((actual_number - 1) * "*")
            lower_row_even = (actual_number * "-") + lower_row_even + ((actual_number -1) * "-")

    counter_1 = actual_number
    while counter_1 > 0:
        if counter_1 % 2 != 0:
            print(upper_row_odd)
        else:
            print(upper_row_even)
        counter_1 -= 1

    middle_print = ""
    middle_print = (actual_number + 1) * " " + "@"
    print(middle_print)

counter_2 = actual_number
while counter_2 > 0:
    if counter_2 % 2 != 0:
        print(lower_row_odd)
    else:
        print(lower_row_even)
    counter_2 -= 1
