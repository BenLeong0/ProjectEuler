year = 1900
day = 0       # Monday
count = 0

start_days = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
    month_lengths[1] = 29
else:
    month_lengths[1] = 28
for i in range(len(start_days)):
    start_days[i] = (start_days[i - 1] + month_lengths[i - 1]) % 7
year += 1

while year <= 2000:
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and year % 400 != 0:
        month_lengths[1] = 29
    else:
        month_lengths[1] = 28

    for i in range(len(start_days)):
        start_days[i] = (start_days[i - 1] + month_lengths[i - 1]) % 7

    count += start_days.count(6)
    year += 1

print(count)
