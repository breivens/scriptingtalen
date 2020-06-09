from calendar import month_name

day, month, year = int(input()), input(), int(input()) - 2000

"""
maanden = ["december", "januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september",
           "oktober", "november"]
maand_index = maanden.index(month)

print(f"Stopwatchbaby's zijn {day} dag{'' if day == 1 else 'en'}, {maand_index} maand{'' if maand_index == 1 else 'en'}"
    f" en {year if maand_index > 0 else year + 1} ja{'ar' if year == 1 or (maand_index == 0 and year == 0) else 'ren'} "
    f"oud op {day} {month} {year + 2000}.")
"""
months = ['december'] + list(map(str.lower, month_name))[1:-1]
month_index = months.index(month)

print(f"Stopwatch babies are {day} day{'' if day == 1 else 's'}, "
      f"{month_index} month{'' if month_index == 1 else 's'} and "
      f"{year if month_index > 0 else year + 1} year{'' if year == 1 or (month_index == 0 and year == 0) else 's'}"
      f" old on {day} {month} {year + 2000}.")
