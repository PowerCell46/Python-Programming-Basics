budget_of_the_movie = float(input())
number_of_extras = int(input())
price_for_one_extra = float(input())
decor_for_the_movie = budget_of_the_movie / 10

if number_of_extras > 150:
    price_for_one_extra -= (price_for_one_extra / 10)

sum_of_extras_expenses = number_of_extras * price_for_one_extra

sum_of_expenses = decor_for_the_movie + sum_of_extras_expenses

if budget_of_the_movie >= sum_of_expenses:
    print("Action!")
    left_money = budget_of_the_movie - sum_of_expenses
    print(f'Wingard starts filming with {left_money:.2f} leva left.')
else:
    print(f'Not enough money!')
    needed_money = sum_of_expenses - budget_of_the_movie
    print(f'Wingard needs {needed_money:.2f} leva more.')
