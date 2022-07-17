def add_time(start, duration, day=''):
    # Initialize variables
    start_time = start.split(':')[:2]
    start_time[1] = start_time[1].split(' ')[0]  # Remove the AM/PM
    duration_time = duration.split(':')
    
    start_hour, start_minute = [int(time) for time in start_time]
    duration_hour, duration_minute = [int(time) for time in duration_time]
    days = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
    days_next = str()

    # Convert PM to 24-hour time
    if start[-2:] == 'PM':
        start_hour = start_hour + 12

    # Add the duration time to the start time
    total_minute = start_minute + duration_minute
    total_hour = start_hour + duration_hour + total_minute // 60
    total_minute = '{:02d}'.format(total_minute % 60)

    temp_hour = total_hour % 12
    if temp_hour > 12:
        total_minute = str(total_minute) + ' PM'
    else:
        total_minute = str(total_minute) + ' AM'

    # Check if the result will be the next day
    if total_hour >= 24:
        total_hour = total_hour - 24
        total_minute += ' (next day)'
        if day:
            day = days[(days.index(day) + 1) % 7]

    # Check if the result will be more than one day later
    if total_hour >= 48:
        total_hour = total_hour - 24
        total_day = total_hour // 24
        total_hour = total_hour % 24
        days_next = '(' + total_day + ' days later)'

    # Return the result
    new_time = '{}:{} {} {}'.format(total_hour, total_minute, day, days_next)

    return new_time