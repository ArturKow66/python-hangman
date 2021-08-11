current_utc = 10.5
time_zone = int(input())

difference = current_utc + float(time_zone)

if difference < 0:
    print('Monday')
elif difference > 24:
    print('Wednesday')
else:
    print('Tuesday')
