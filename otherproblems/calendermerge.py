input1 = [['09:00', '10:30'],
          ['12:00', '13:00'],
          ['16:00', '18:00']]
bounds1 = ['09:00', '20:00']

input2 = [['10:00', '11:30'],
          ['12:30', '14:30'],
          ['14:30', '15:00'],
          ['16:00', '17:00']]
bounds2 = ['10:00', '18:30']

mtime = 30


def calenderAvail(p1Sched, p2Sched, p1Bounds, p2Bounds, time):
    booked_times = []
    if timeToMins(p1Bounds[0]) < timeToMins(p2Bounds[0]):
        booked_times.append(['00:00', p2Bounds[0]])
    else:
        booked_times.append(['00:00', p1Bounds[0]])
    p1, p2 = 0, 0
    while p1 < len(p1Sched) or p2 < len(p2Sched):
        if p1 == len(p1Sched):
            booked_times.append(p2Sched[p2])
            p2+=1
        elif p2 == len(p2Sched):
            booked_times.append(p1Sched[p1])
            p1+=1
        elif timeToMins(p1Sched[p1][0]) < timeToMins(p2Sched[p2][0]):
            booked_times.append(p1Sched[p1])
            p1 += 1
        else:
            booked_times.append(p2Sched[p2])
            p2 += 1
        mergeFinalTwo(booked_times)
    if timeToMins(p1Bounds[1]) < timeToMins(p2Bounds[1]):
        booked_times.append([p1Bounds[1], "24:00"])
    else:
        booked_times.append([p2Bounds[1], "24:00"])
    mergeFinalTwo(booked_times)
    free_times = []
    for n in range(len(booked_times)-1):
        slot = [booked_times[n][1], booked_times[n+1][0]]
        if timeToMins(slot[1]) - timeToMins(slot[0]) >= time:
            free_times.append(slot)
    return free_times


def timeToMins(t):
    hour, minute = t.split(':')
    return int(hour) * 60 + int(minute)

def minsToTime(m):
    hour, minute = int(m/60), m%60
    return "{:02d}".format(hour) + ':' + "{:02d}".format(minute)

def mergeFinalTwo(calender):
    if timeToMins(calender[-1][0]) <= timeToMins(calender[-2][1]):
        if timeToMins(calender[-2][1]) > timeToMins(calender[-1][1]):
            merged = [calender[-2][0], calender[-2][1]]
        else:
            merged = [calender[-2][0], calender[-1][1]]
        calender[-2] = merged
        del calender[-1]


print(calenderAvail(input1, input2, bounds1, bounds2, mtime))
