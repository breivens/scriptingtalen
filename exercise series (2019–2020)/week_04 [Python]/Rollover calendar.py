from datetime import date
from calendar import monthrange

current = date.today()


# w/ dims
def rolloverDate(day=current.day, month=current.month, year=current.year):
    if month > 12:
        year += month // 12
        month %= 12
    while day > (dim := monthrange(year, month)[1]):
        day -= dim  # Days In Month
        month += 1
        if month > 12:
            year += month // 12
            month %= 12
    return date(year, month, day)


# w/ monthrange
def rolloverDate2(day=current.day, month=current.month, year=current.year):
    if month > 12:
        year += month // 12
        month %= 12
    while day > (dim := monthrange(year, month)[1]):
        day -= dim  # Days In Month
        month += 1
        if month > 12:
            year += month // 12
            month %= 12
    return date(year, month, day)
