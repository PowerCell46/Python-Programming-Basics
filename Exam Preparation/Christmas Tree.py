import copy

input_number = int(input())

last_row_list = []

list_print = [" ", "|", " "]

for i in range(0, input_number):
    list_print.append("*")
    list_print.insert(0, "*")
    if i == (input_number - 1):
        last_row_list = list_print

reversed_list = copy.deepcopy(last_row_list)
n = 0
print_row = copy.deepcopy(last_row_list)

while "*" in last_row_list:
    n += 1
    index_1 = last_row_list.index("*")
    last_row_list.pop(index_1)
    last_row_list.insert(index_1, " ")

    index_2 = len(last_row_list) - n
    last_row_list.pop(index_2)
    last_row_list.insert(index_2, " ")
    copy_list = copy.deepcopy(last_row_list)
    reversed_list.append(copy_list)

for index in range((len(reversed_list) - 1), -1, -1):
    if index == (len(reversed_list) - input_number -1):
        break
    current_list = reversed_list[index]
    print("".join(current_list))

print("".join(print_row))
