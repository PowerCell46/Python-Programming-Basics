input_num = float(input())
first_word = ""

if input_num == 0:
    print("zero")
elif input_num > 0:

    if input_num < 1:
        print("small posivite")
    elif input_num > 1000000:
        print("large posivite")
    else:
        print("positive")

elif input_num < 0:
    if input_num > -1:
        print("small negative")
    elif input_num < -1000000:
        print("large negative")
    else:
        print("negative")
