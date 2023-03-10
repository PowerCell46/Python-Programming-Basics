hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

start_of_the_exam = hour_of_the_exam * 60 + minute_of_the_exam
coming_to_the_exam = hour_of_arrival * 60 + minute_of_arrival
output = ""
final_minutes = 0
final_hours = 0

if coming_to_the_exam <= start_of_the_exam and start_of_the_exam - coming_to_the_exam <= 30: ## On time
    output = "On time"
    final_minutes = start_of_the_exam - coming_to_the_exam
    if final_minutes == 0:
        print(output)
    else:
        print(output)
        print((f'{final_minutes} minutes before the start'))

elif start_of_the_exam - coming_to_the_exam > 30: ## Early
    output = "Early"
    final_minutes = start_of_the_exam - coming_to_the_exam
    if final_minutes >= 60:
        while final_minutes >= 60:
            final_minutes -= 60
            final_hours += 1
        print(output)
        if final_minutes < 10:
            print(f'{final_hours}:0{final_minutes} hours before the start')
        else:
            print(f'{final_hours}:{final_minutes} hours before the start')
    else:
        print(output)
        print(f'{final_minutes} minutes before the start')

elif coming_to_the_exam > start_of_the_exam:
    output = "Late"
    final_minutes = coming_to_the_exam - start_of_the_exam
    if final_minutes >= 60:
        while final_minutes >= 60:
            final_minutes -= 60
            final_hours += 1
        print(output)
        if final_minutes < 10:
            print(f'{final_hours}:0{final_minutes} hours after the start')
        else:
            print(f'{final_hours}:{final_minutes} hours after the start')
    else:
        print(output)
        print(f'{final_minutes} minutes after the start')
