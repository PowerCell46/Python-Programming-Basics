number_of_groups_of_climbers = int(input())

all_people = 0
musala_counter = 0
mondblan_counter = 0
kilimanjaro_counter = 0
k2_counter = 0
everest_counter = 0

for index in range(0, number_of_groups_of_climbers):
    current_group = int(input())
    all_people += current_group

    if current_group <= 5:
        musala_counter += current_group
    elif current_group > 5 and current_group <= 12:
        mondblan_counter += current_group
    elif current_group > 12 and current_group <= 25:
        kilimanjaro_counter += current_group
    elif current_group > 25 and current_group <= 40:
        k2_counter += current_group
    elif current_group > 40:
        everest_counter += current_group

one_percent = all_people / 100
musala_counter = musala_counter / one_percent
print(f'{musala_counter:.2f}%')
mondblan_counter = mondblan_counter / one_percent
print(f'{mondblan_counter:.2f}%')
kilimanjaro_counter = kilimanjaro_counter / one_percent
print(f'{kilimanjaro_counter:.2f}%')
k2_counter = k2_counter / one_percent
print(f'{k2_counter:.2f}%')
everest_counter = everest_counter / one_percent
print(f'{everest_counter:.2f}%')
