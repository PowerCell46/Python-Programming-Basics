number_of_floors = int(input())
number_of_rooms = int(input())

for floor in range(number_of_floors, 0, -1):
    if floor == number_of_floors:
        current_floor = "L"
    elif floor % 2 == 0:
        current_floor = "O"
    elif floor % 2 != 0:
        current_floor = "A"
    current_print = ""
    for room in range(0, number_of_rooms):
        current_print += (f'{current_floor}{floor}{room} ')
    print(current_print)
