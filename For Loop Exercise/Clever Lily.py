import math

age = int(input())
washing_machine_price = float(input())
price_for_a_toy = int(input())
number_of_toys = 0
colected_money = 0
current_money = 0
for current_age in range(1, age + 1):
    if current_age % 2 != 0:
        number_of_toys += 1
    else:
        current_money += 10
        colected_money += current_money
        colected_money -= 1

colected_money += (number_of_toys * price_for_a_toy)

if colected_money >= washing_machine_price:
    left_money = math.fabs(colected_money - washing_machine_price)
    print(f'Yes! {left_money:.2f}')
else:
    needed_money = math.fabs(washing_machine_price - colected_money)
    print(f'No! {needed_money:.2f}')
