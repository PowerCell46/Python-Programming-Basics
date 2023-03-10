width = int(input())
height = int(input())
cake_size = width * height
current_parts = str(input())
taken_parts = 0

while True:
    if current_parts == "STOP":
        break
    current_parts = int(current_parts)
    taken_parts += current_parts
    if taken_parts >= cake_size:
        break
    current_parts = str(input())

if taken_parts > cake_size:
    needed_parts = taken_parts - cake_size
    print(f'No more cake left! You need {needed_parts} pieces more.')
else:
    left_parts = cake_size - taken_parts
    print(f'{left_parts} pieces are left.')
