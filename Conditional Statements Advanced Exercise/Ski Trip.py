number_of_days = int(input()) - 1
room_type = str(input())
review = str(input())
price = 0
discount = 0

if room_type == "room for one person":
    price = 18

    if number_of_days < 10:
        discount = 0
    elif number_of_days >= 10 and number_of_days <= 15:
        discount = 0
    elif number_of_days > 15:
        discount = 0


elif room_type == "apartment":
    price = 25


    if number_of_days < 10:
        discount = 30
    elif number_of_days >= 10 and number_of_days <= 15:
        discount = 35
    elif number_of_days > 15:
        discount = 50

elif room_type == "president apartment":
    price = 35


    if number_of_days < 10:
        discount = 10
    elif number_of_days >= 10 and number_of_days <= 15:
        discount = 15
    elif number_of_days > 15:
        discount = 20

sum = price * number_of_days - ((price * number_of_days / 100) * discount)

if review == "positive":
    discount = 25
    sum += ((sum / 100) * discount)
elif review == "negative":
    discount = 10
    sum -= ((sum / 100) * discount)

print(f'{sum:.2f}')
