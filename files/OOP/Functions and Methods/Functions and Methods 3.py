

# 17.2 Printing objects

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    # 17.2 result
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):

    final = Time()
    minutes = 0

    if seconds < 60:
        final.second = seconds
    else:
        minutes = int(seconds / 60)
        final.second = seconds % 60

    if minutes < 60:
        final.minute = minutes
    else:
        hours = int(minutes / 60)
        final.minute = minutes % 60
        final.hour = hours

    return final

# 17.6 The __str__ method

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y)
        else:
            new_x = self.x + other[0]
            new_y = self.y + other[1]
            return Point(new_x, new_y)

    def __radd__(self, other):
        return self.__add__(other)

# 17.10 Debugging

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

start = Time(9, 45)
start.print_time()

end = start.increment(1337)
end.print_time()
print(end.is_after(start))

# 17.5 result
p1 = Point(10, 20)

# 17.6 result
print(p1)

# 17.7 result
duration = Time(1, 35)
print(start + duration)

p2 = Point(100, 200)
print(p1 + p2)

# 17.8 test and result
print(start + duration)
print(start + 1337)
print(1337 + start)

print(p1 + p2)
print(p1 + (10, 20))







