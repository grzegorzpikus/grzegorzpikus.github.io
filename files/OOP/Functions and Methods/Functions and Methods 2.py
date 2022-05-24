# As an exercise, write a function called print_time that takes a Time object
# and prints it in the form hour:minute:second.

# 16.1 Time

class Time:

     hour = 0
     minute = 0
     second = 0

def print_time(time : Time):
    print(f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

def is_after(t1 : Time, t2 : Time):
    if t2.hour > t1.hour:
        return True
    elif t2.hour == t1.hour:
        if t2.minute > t1.minute:
            return True
        elif t2.minute == t1.minute:
            if t2.second > t1.second:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# 16.2 Pure functions

def add_time(t1 : Time, t2 : Time):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


# 16.3 Modifiers

def increment(time, seconds):
    final = Time()
    final.second = time.second + seconds

    if final.second >= 60:
        additional_minutes = int(final.second / 60)
        final.second = final.second % 60
        final.minute = time.minute + additional_minutes

    if final.minute >= 60:
        additional_hour = int(final.minute / 60)
        minute_left = final.minute % 60
        final.minute = minute_left
        final.hour = additional_hour + time.hour

    return print_time(final)

# 16.4 Prototyping versus planning

def time_to_int(time : Time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

# 16.5 Debugging

def valid_time(time : Time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time_2(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def int_to_time(seconds):
    new_time = Time()
    if seconds < 60:
        new_time.second = seconds
    else:
        new_time.second = seconds % 60


    if int(seconds / 60) < 60:
        new_time.minute = int(seconds / 60)
    else:
        new_time.minute = (int(seconds / 60)) % 60

    new_time.hour = int(new_time.minute / 60)

    return new_time

t = Time()
t.hour = 1
t.minute = 50
t.second = 50

t2 = Time()
t2.hour = 1
t2.minute = 40
t2.second = 40
t2_total_seconds = time_to_int(t2)

# 16.1 Time - the result
print_time(t2)
print(is_after(t, t2))

# 16.3 Modifiers - the result
increment(t, t2_total_seconds)



