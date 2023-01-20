width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
total_free_space = width_of_free_space * length_of_free_space * height_of_free_space

current_boxes = str(input())
sum_of_boxes = 0

while True:
    current_boxes = int(current_boxes)
    sum_of_boxes += current_boxes
    if sum_of_boxes >= total_free_space:
        break
    current_boxes = str(input())
    if current_boxes == "Done":
        break


if sum_of_boxes >= total_free_space:
    needed_space = sum_of_boxes - total_free_space
    print(f'No more free space! You need {needed_space} Cubic meters more.')
else:
    left_space = total_free_space - sum_of_boxes
    print(f'{left_space} Cubic meters left.')
