import math

n = int(input())
sum1 = 0
counter = 0
sum2 = 0

for index in range(0, n):
    current_num = int(input())
    sum1 += current_num
    counter += 1

for index1 in range(counter, 2 * n):
    current_num = int(input())
    sum2 += current_num

if sum1 == sum2:
    print(f'Yes, sum = {sum2}')
else:
    difference = math.fabs(sum2 - sum1)
    difference = math.trunc(difference)
    print(f'No, diff = {difference}')
