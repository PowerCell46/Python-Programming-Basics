goal_jump_height = int(input())
current_goal_jump_height = goal_jump_height - 30
fail_counter = 0
jump_counter = 0

while True:

    current_jump_height = int(input())
    jump_counter += 1
    if current_jump_height > goal_jump_height and current_goal_jump_height >= goal_jump_height:
        print(f'Tihomir succeeded, he jumped over {current_goal_jump_height}cm after {jump_counter} jumps.')
        break
    if current_jump_height > current_goal_jump_height:
        current_goal_jump_height += 5
        fail_counter = 0
    else:
        fail_counter += 1
        if fail_counter == 3:
            print(f'Tihomir failed at {current_goal_jump_height}cm after {jump_counter} jumps.')
            break
