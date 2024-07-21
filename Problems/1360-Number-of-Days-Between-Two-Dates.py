class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def calc_days(year, month, day):
            days = 0
            months = {
                1: 31, 2: 29 if is_leap_year(year) else 28,
                3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                9: 30, 10: 31, 11: 30, 12: 31
            }

            for y in range(1971, year):
                days += 366 if is_leap_year(y) else 365

            for m in range(1, month):
                days += months[m]

            days += day

            return days


        year1, month1, day1 = map(int, date1.split('-'))
        year2, month2, day2 = map(int, date2.split('-'))

        return abs(calc_days(year1, month1, day1) - calc_days(year2, month2, day2))
