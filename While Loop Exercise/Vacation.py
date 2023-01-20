needed_money = float(input())
current_money = float(input())
action = str(input())
current_sum = float(input())
spend_counter = 0
days_counter = 0

while True:
    days_counter += 1

    if action == "save":
        current_money += current_sum
        spend_counter = 0
        if current_money >= needed_money:
            break
    elif action == "spend":
        current_money -= current_sum
        if current_money < 0:
            current_money = 0
        spend_counter += 1
        if spend_counter == 5:
            print("You can't save the money.")
            print(f'{days_counter}')
            break
    action = str(input())
    current_sum = float(input())

if current_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')
