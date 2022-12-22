final_number = int(input("Enter where you want the function to stop: "))
numbers_list = [0, 1]
current_number = 0
current_index = 2
while True:
    current_number = numbers_list[current_index - 2] + numbers_list[current_index - 1]
    if current_number > final_number:
        break
    numbers_list.append(current_number)
    current_index += 1

print(numbers_list)