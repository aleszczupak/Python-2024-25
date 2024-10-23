class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return '{} sec'.format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print('{} {}'.format(time1, time2)) # Python wywołuje str()
print('{}'.format([time1, time2])) # Python wywołuje repr()

# 12 sec 3456 sec
# [Time(12), Time(3456)]

class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __repr__(self):
        return 'Time({})'.format(self.s)

time1 = Time(12)
time2 = Time(3456)
print('{} {}'.format(time1, time2))
print('{}'.format([time1, time2]))

# Time(12) Time(3456)
# [Time(12), Time(3456)]

class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return '{} sec'.format(self.s)

time1 = Time(12)
time2 = Time(3456)
print('{} {}'.format(time1, time2))
print('{}'.format([time1, time2]))

# 12 sec 3456 sec
# [<__main__.Time object at 0x0000025624528C50>, <__main__.Time object at 0x0000025623DCD210>]
