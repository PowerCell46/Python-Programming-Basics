import copy

input_number = int(input())

if input_number == 1:
    print("*")
else:
    middle_row_list = []

    for i in range(0, input_number):
        if i == 0 or i == (input_number - 1):
            middle_row_list.append("*")
        else:
            middle_row_list.append("-")

    list_of_rows = []
    middle_row_print = copy.deepcopy(middle_row_list)

    index = -1

    if input_number % 2 == 0:
        while middle_row_list[input_number // 2] != "*" and middle_row_list[input_number // 2 - 1] != "*":
            index += 1
            middle_row_list.pop(index)
            middle_row_list.insert(index, "-")
            middle_row_list.pop(len(middle_row_list) - (index + 1))
            middle_row_list.insert(len(middle_row_list) - (index + 1), "-")

            middle_row_list.pop(index + 1)
            middle_row_list.insert((index + 1), "*")
            middle_row_list.pop(len(middle_row_list) - (index + 2))
            middle_row_list.insert(len(middle_row_list) - (index + 1), "*")
            copy_list = copy.deepcopy(middle_row_list)
            list_of_rows.append(copy_list)

    else:
        while (input_number - 1) // 2 != "*":
            index += 1
            middle_row_list.pop(index)
            middle_row_list.insert(index, "-")

            middle_row_list.pop(index + 1)
            middle_row_list.insert((index + 1), "*")

            if middle_row_list[(input_number - 1) // 2] == "*":
                middle_row_list.pop(index + 2)
                middle_row_list.insert(index + 2, "-")
                copy_list = copy.deepcopy(middle_row_list)
                list_of_rows.append(copy_list)
                break

            middle_row_list.pop(len(middle_row_list) - (index + 1))
            middle_row_list.insert(len(middle_row_list) - (index + 1), "-")

            middle_row_list.pop(len(middle_row_list) - (index + 2))
            middle_row_list.insert(len(middle_row_list) - (index + 1), "*")

            copy_list = copy.deepcopy(middle_row_list)
            list_of_rows.append(copy_list)

    for i in range((len(list_of_rows) - 1), -1, -1):
        current_row = list_of_rows[i]
        print("".join(current_row))

    print("".join(middle_row_print))

    for i in range(0, len(list_of_rows)):
        current_row = list_of_rows[i]
        print("".join(current_row))
