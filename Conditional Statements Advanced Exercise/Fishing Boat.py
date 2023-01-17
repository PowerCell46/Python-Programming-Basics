budget = int(input())
season = str(input())
number_of_fishers = int(input())
price = 0
discount = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_of_fishers <= 6:
    discount = 10
elif number_of_fishers >= 7 and number_of_fishers <= 11:
    discount = 15
elif number_of_fishers >= 12:
    discount = 25

sum = price - ((price / 100) * discount)

if number_of_fishers % 2 == 0 and season != "Autumn":
    discount = 5
    sum = sum - ((sum / 100) * discount)

if budget >= sum:
    left_money = budget - sum
    print(f'Yes! You have {left_money:.2f} leva left.')
else:
    needed_money = sum - budget
    print(f'Not enough money! You need {needed_money:.2f} leva.')
