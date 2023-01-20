goal_steps = 10000
current_steps = str(input())
sum_of_steps = 0

while True:
    if current_steps == "Going home":
        current_steps = int(input())
        sum_of_steps += current_steps
        break
    current_steps = int(current_steps)
    sum_of_steps += current_steps
    if sum_of_steps >= goal_steps:
        break
    current_steps = str(input())

if sum_of_steps < goal_steps:
    needed_steps = goal_steps - sum_of_steps
    print(f'{needed_steps} more steps to reach goal.')
else:
    bonus_steps = sum_of_steps - goal_steps
    print(f'Goal reached! Good job!')
    print(f'{bonus_steps} steps over the goal!')
