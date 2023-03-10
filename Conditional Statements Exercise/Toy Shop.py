excursion_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
number_of_toys = number_of_trucks + number_of_minions + number_of_bears + number_of_dolls + number_of_puzzles
puzzles_price = number_of_puzzles * 2.60
dolls_price = number_of_dolls * 3
bears_price = number_of_bears * 4.10
minions_price = number_of_minions * 8.20
trucks_price = number_of_trucks * 2
sum_of_prices = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

if number_of_toys >= 50:
    sum_of_prices -= ((sum_of_prices / 100) * 25)

sum_of_prices -= (sum_of_prices / 10)

if sum_of_prices >= excursion_price:
    left_money = sum_of_prices - excursion_price
    print(f'Yes! {left_money:.2f} lv left.')
else:
    needed_money = excursion_price - sum_of_prices
    print(f'Not enough money! {needed_money:.2f} lv needed.')
