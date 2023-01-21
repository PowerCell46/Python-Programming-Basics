prime_sum = 0
non_prime_sum = 0
stop_is_used = False
while True:
    the_number_is_prime = True
    current_number = str(input())
    if current_number == "stop":
        stop_is_used = True
        break
    current_number = int(current_number)
    if current_number < 0:
        print("Number is negative.")
        continue
    divider = current_number - 1
    while divider > 1:
        if current_number % divider == 0:
            non_prime_sum += current_number
            the_number_is_prime = False
            break
        else:
            the_number_is_prime = True
        divider -= 1
    if the_number_is_prime == True:
        prime_sum += current_number


if stop_is_used == True:
    print(f'Sum of all prime numbers is: {prime_sum}')
    print(f'Sum of all non prime numbers is: {non_prime_sum}')
