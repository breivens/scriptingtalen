from datetime import date, timedelta


def rolloverDate2(day=None, month=None, year=None):
    current = date.today() if None in (day, month, year) else None
    year, month, day = year or current.year, month or current.month, day or current.day
    year += (month - 1) // 12
    return date(year, 1 + (month - 1) % 12, 1) + timedelta(day - 1)
