fruit = str(input())
day_of_the_week = str(input())
quantity = float(input())
price = 0
there_is_an_error = False

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday":

    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        print("error")
        there_is_an_error = True

elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":

    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        print("error")
        there_is_an_error = True

else:
    there_is_an_error = True
    print("error")

if there_is_an_error == False:
    sum = price * quantity
    print(f'{sum:.2f}')
else:
    print()
