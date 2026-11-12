day_number = int(input())

day = ''

if day_number == 1:
    day = 'Sunday'
elif day_number == 2:
    day = 'Monday'
elif day_number == 3:
    day = 'Tuesday'
elif day_number == 4:
    day = 'Wednesday'
elif day_number == 5:
    day = 'Thursday'
elif day_number == 6:
    day = 'Friday'
elif day_number == 7:
    day = 'Saturday'
else:
    print('invalid argument')
    
print(day)