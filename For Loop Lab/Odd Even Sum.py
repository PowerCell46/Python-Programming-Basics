import math

number_of_numbers = int(input())
even_sum = 0
odd_sum = 0

for index in range(1, number_of_numbers + 1):
    current_num = int(input())
    if index % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    difference = math.fabs(even_sum - odd_sum)
    difference = math.trunc(difference)
    print(f'Diff = {difference}')
