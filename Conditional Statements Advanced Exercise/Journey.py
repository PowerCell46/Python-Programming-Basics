budget = float(input())
season = str(input())
percentage = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        percentage = 30
        place = "Camp"
    elif season == "winter":
        percentage = 70
        place = "Hotel"

elif budget > 100 and budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        percentage = 40
        place = "Camp"
    elif season == "winter":
        percentage = 80
        place = "Hotel"

elif budget > 1000:
    destination = "Europe"
    percentage = 90
    place = "Hotel"

print(f'Somewhere in {destination}')
spent_money = (budget / 100) * percentage
print(f'{place} - {spent_money:.2f}')
