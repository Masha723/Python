
"""
a function is_available_date() that takes two arguments in the following order:
booked_dates is a list of string dates that are not available for booking. 
The list element is either a single date or a period (two dates separated by a hyphen).
For example: ['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking - A single string date or period (two dates separated by a hyphen)
for which the guest wishes to book. 
For example: '11/01/2021' or '11/01/2021-11/04/2021'
The  function returns True if the date or period date_for_booking is fully available for booking.
Otherwise, the function returns False.

"""

def is_available_date(dates,some_dates):
    from datetime import date
    result=set()
    result1=set()
    for i in dates:
        if '-' in i:
            k=i.split('-')
            day,month,year=k[0].split('.')
            day1,month1,year1=k[1].split('.')
            first=date(int(year),int(month),int(day))
            second=date(int(year1),int(month1),int(day1))
            for j in range(first.toordinal(),second.toordinal()+1):
                result.add(date.fromordinal(j))
        else:
            day,month,year=i.split('.')
            result.add(date(int(year),int(month),int(day)))

    if '-' in some_dates:
        some_dates=some_dates.split('-')
        day,month,year=some_dates[0].split('.')
        day1,month1,year1=some_dates[1].split('.')
        first=date(int(year),int(month),int(day))
        second=date(int(year1),int(month1),int(day1))
        for j in range(first.toordinal(),second.toordinal()+1):
            result1.add(date.fromordinal(j))
    else:
        day,month,year=some_dates.split('.')
        result1.add(date(int(year),int(month),int(day)))           
    if result&result1==set():
        return True
    else:
        return False


"""
Test samples
"""

dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))


dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))


dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))









