city = str(input())
number_of_sales = float(input())
percentage = 0
there_is_an_error = False

if city == "Sofia":

    if number_of_sales >= 0 and number_of_sales <= 500:
        percentage = 5
    elif number_of_sales > 500 and number_of_sales <= 1000:
        percentage = 7
    elif number_of_sales > 1000 and number_of_sales <= 10000:
        percentage = 8
    elif number_of_sales > 10000:
        percentage = 12
    else:
        there_is_an_error = True

elif city == "Varna":

    if number_of_sales >= 0 and number_of_sales <= 500:
        percentage = 4.5
    elif number_of_sales > 500 and number_of_sales <= 1000:
        percentage = 7.5
    elif number_of_sales > 1000 and number_of_sales <= 10000:
        percentage = 10
    elif number_of_sales > 10000:
        percentage = 13
    else:
        there_is_an_error = True

elif city == "Plovdiv":

    if number_of_sales >= 0 and number_of_sales <= 500:
        percentage = 5.5
    elif number_of_sales > 500 and number_of_sales <= 1000:
        percentage = 8
    elif number_of_sales > 1000 and number_of_sales <= 10000:
        percentage = 12
    elif number_of_sales > 10000:
        percentage = 14.5
    else:
        there_is_an_error = True
else:
    there_is_an_error = True



if there_is_an_error == False:
    profit = number_of_sales / 100 * percentage

    print(f'{profit:.2f}')
else:
    print("error")
