flowers_type = str(input())
number_of_flowers = int(input())
budget = int(input())
price = 0
discount = 0
pricing = 0
sum = 0

if flowers_type == "Roses":
    price = 5
elif flowers_type == "Dahlias":
    price = 3.80
elif flowers_type == "Tulips":
    price = 2.80
elif flowers_type == "Narcissus":
    price = 3
elif flowers_type == "Gladiolus":
    price = 2.50

if flowers_type == "Roses" and number_of_flowers > 80:
    discount = 10
    sum = number_of_flowers * price
    sum = sum - ((sum / 100) * discount)
elif flowers_type == "Dahlias" and number_of_flowers > 90:
    discount = 15
    sum = number_of_flowers * price
    sum = sum - ((sum / 100) * discount)
elif flowers_type == "Tulips" and number_of_flowers > 80:
    discount = 15
    sum = number_of_flowers * price
    sum = sum - ((sum / 100) * discount)
elif flowers_type == "Narcissus" and number_of_flowers < 120:
    pricing = 15
    sum = number_of_flowers * price
    sum = sum + ((sum / 100) * pricing)
elif flowers_type == "Gladiolus" and number_of_flowers < 80:
    pricing = 20
    sum = number_of_flowers * price
    sum = sum + ((sum / 100) * pricing)
else:
    sum = number_of_flowers * price

if sum <= budget:
    left_money = budget - sum
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers_type} and {left_money:.2f} leva left.')
elif sum > budget:
    needed_money = (sum - budget)
    print(f'Not enough money, you need {needed_money:.2f} leva more.')
