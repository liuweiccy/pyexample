# 将以数指定年、月、日的日期打印出来
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 一个列表，其中包含1~31对应的尾数
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']

year = input('Year:')
month = int(input('Month(1-12):'))
day = int(input('Day(1-31):'))

month_name = months[month - 1]
ordinal = str(day) + endings[day - 1]

print(month_name + " " + ordinal + ", " + year)
