month = str(input())
number_of_nights = int(input())
studio_price_for_a_night = 0
apartment_price_for_a_night = 0
studio_discount = 0
apartment_discount = 0

if month == "May" or month == "October":
    studio_price_for_a_night = 50
    apartment_price_for_a_night = 65
    if number_of_nights > 7 and number_of_nights <= 14:
        studio_discount = 5
    elif number_of_nights > 14:
        studio_discount = 30
        apartment_discount = 10

elif month == "June" or month == "September":
    studio_price_for_a_night = 75.20
    apartment_price_for_a_night = 68.70
    if number_of_nights > 14:
        studio_discount = 20
        apartment_discount = 10

elif month == "July" or month == "August":
    studio_price_for_a_night = 76
    apartment_price_for_a_night = 77
    if number_of_nights > 14:
        apartment_discount = 10


apartment_final_price = (apartment_price_for_a_night * number_of_nights) - ((apartment_price_for_a_night * number_of_nights / 100) * apartment_discount)
print(f'Apartment: {apartment_final_price:.2f} lv.')

studio_final_price = (studio_price_for_a_night * number_of_nights) - ((studio_price_for_a_night * number_of_nights / 100) * studio_discount)
print(f'Studio: {studio_final_price:.2f} lv.')
