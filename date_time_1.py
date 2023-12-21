"""
A list of employees contains their last and first names, and dates of birth. 
The program determines the youngest employee who celebrates his birthday
within the next seven days from the current date.

Input format
The input to the program in the first line is the current date in the format DD.MM.YYYY,
in the next line the natural number n is entered - the number of employees
working in the organization. In the next n lines, data about each employee is entered:
first name, last name and date of birth, separated by a space. Date of birth is
indicated in the format DD.MM.YYYY.

Output format
The program determines the youngest employee celebrating his birthday
within the next seven days, and display his first and last name, separated by a space. 
If there are no such employees, the program should output the text: No birthdays planned


"""




from datetime import date, time, datetime, timedelta
d,m,y=input().split('.')
number=int(input())
start=date(int(y),int(m),int(d))
end=start.toordinal()+7
end=date.fromordinal(end)
di=dict()
for i in range(number):
    i=input().split()
    day,month,year=i[2].split('.')
    one=i[0]+' '+i[1]
    two=date(int(year),int(month),int(day))
    if int(month) in [2,3,4,5,6,7,8,9,10,11,12]:
        three=date(int(y),int(month),int(day))
        if start<three<=end:
            di[one]=two.toordinal()
    else:
        three=date(int(y)+1,int(month),int(day))
        if start<three<=end:
            di[one]=two.toordinal()

if len(di)>0:
    p=max(di.items(),key = lambda x: x[1])
    print(p[0])
else:
    print('No birthdays planned')


"""
Input examples

Sample 1

12.11.2021
5
SAM POI 14.10.1995
ANDREW UO 29.04.1992
KIM KARDASHIAN 23.11.1996
Bruce Wow 19.11.1994
Mary Poppins 16.07.1995

Sample 2

14.11.2021
3
David Petr 16.11.1995
Petr Pavel 22.11.1997
Yin Yan 17.11.1994

"""


    
