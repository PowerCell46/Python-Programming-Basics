retruned_money = float(input())
coins = 0

while retruned_money - 2 >= 0:
    retruned_money -= 2
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 1 >= 0:
    retruned_money -= 1
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.50 >= 0:
    retruned_money -= 0.50
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.20 >= 0:
    retruned_money -= 0.20
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.10 >= 0:
    retruned_money -= 0.10
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.05 >= 0:
    retruned_money -= 0.05
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.02 >= 0:
    retruned_money -= 0.02
    retruned_money = round(retruned_money, 2)
    coins += 1
while retruned_money - 0.01 >= 0:
    retruned_money -= 0.01
    retruned_money = round(retruned_money, 2)
    coins += 1

print(coins)
