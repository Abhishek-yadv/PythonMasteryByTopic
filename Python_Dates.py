####################################################################
############################################################ (Dates)
####################################################################

##########################################################
######################################### (time module)
######## Functions
#! sleep() function:
# time.sleep(seconds): Suspends program execution for the specified duration (in seconds).
import time
for i in range(4):
    time.sleep(1)
    print(i)

#! time() Function: -
# time.time(): Returns the current time in seconds since epoch (January 1, 1970).useful for measuring execution time or generating timestamps.
current_time = time.time()
print(f"Current time in seconds since epoch: {current_time:.6f}")
# >>> Current time in seconds since epoch: 1710163167.377825

#! (Converting a Time Object to a String) 
#! time.strftime(format[, t]): stands for “string format time.
# format strings from a given time objet struct_time/Python time tuple
time.strftime('%Y-%m-%d', time.localtime())
# >>> '2019-03-01'

#! asctime(): convert a time tuple/truct_time to a string as returned by gmtime() or localtime() form like 'Sun Jun 20 23:21:05 1993'
# asctime(Tuple or struct_time argument required)
print(time.asctime(time.gmtime()))  # Output : Mon Mar 11 13:49:05 2024
print(time.asctime(time.localtime()))  # Output: Mon Mar 11 19:19:30 2024

print(time.asctime('2019-03-01'))  # Output: Error (Tuple or struct_time argument required


#! Converting a String (time) to an time Object(struct_time) :
#! strptime(string[, format]): “string parse time” convert a time string to a struct_time/time tuple
import time
print(time.strptime('2019-03-01', '%Y-%m-%d'))
# >>> time.struct_time(tm_year=2019, tm_mon=3, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=60, tm_isdst=-1)

#* Both gmtime() and localtime() return struct_time instances, for UTC and local time respectively.
print(time.gmtime())
print(time.localtime())
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=11, tm_hour=13, tm_min=54, tm_sec=17, tm_wday=0, tm_yday=71, tm_isdst=0)
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=11, tm_hour=19, tm_min=24, tm_sec=17, tm_wday=0, tm_yday=71, tm_isdst=0)

#! ctime([secs]) Functions:
# time.ctime():  Getting time string from seconds or Converts a specified timestamp into a human-readable date and time format
import time
timestamp = 1627908313.717886
formatted_time = time.ctime(timestamp)
print(f"Current time: {formatted_time}")
# >>> Current time: Mon Aug  2 18:15:13 2021 <str>

import time
timestamp = 1627908313.717886
formatted_time = time.ctime(23234)
print(formatted_time)  # Output: Thu Jan  1 11:57:14 1970
# If secs is not provided or None, the current time as returned by time() is used.
my_ctime = time.ctime()
print(my_ctime)  # >>> Tue Mar 12 08:39:16 2024

current_time = time.ctime(time.time())
print(current_time) # >>> Mon Mar 11 19:12:50 2024 #str

my_lctime = time.asctime((time.localtime()))
print(my_lctime) # >>> Tue Mar 12 08:39:16 2024

#! time.gmtime(0):
# Retrieves the time in the GMT (Greenwich Mean Time) timezone at the Unix epoch) (January 1, 1970, 00:00:00 UTC).
epoch_time = time.gmtime(0)
print(f"Epoch time: {epoch_time}")
# >>> Epoch time: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

#! time.localtime():
# time.localtime(): Returns a named tuple representing local time (non-epochal timestamps). You can access its values by both index and attribute name.

print(time.localtime())
# >>> time.struct_time(tm_year=2024, tm_mon=3, tm_mday=11, tm_hour=19, tm_min=20, tm_sec=22, tm_wday=0, tm_yday=71, tm_isdst=0)


"""
!class time.struct_time: -
                    The type of the time value sequence returned by gmtime(), localtime(), and strptime().
It is an object with a named tuple interface: values can be accessed by index and by attribute name.
The following values are present:

Index      Attribute    Values
0          tm_year      (for example, 1993)
1          tm_mon       range [1, 12]
2          tm_day       range [1, 31]
3          tm_hour      range [0, 23]
4          tm_min       range [0, 59]
5          tm_sec       range [0, 61]; see Note (2) in strftime()
6          tm_wday      range [0, 6]; Monday is 0
7          tm_yday      range [1, 366]
8          tm_isdst     0, 1 or -1; see below
N/A        tm_zone      abbreviation of timezone name
N/A        tm_gmtoff    offset east of UTC in seconds
"""
# !You can access these attributes using either attribute names or numbers.
# Get the current time as a struct_time object
current_time = time.localtime()
# Access individual components
year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday
print("Year:", year)  # Year: 2024
print("Month:", month)  # Month: 3
print("Day:", day)  # Day: 12

# timeit: A module for measuring the performance of code snippets
# python -m timeit -n 1 -r 0 -s "import datetime, time, calendar" "exec(open('Python_Dates.py', encoding='utf-8').read())"
# python -m timeit "'-'.join(str(n) for n in range(100))"


##########################################################
################################## (calender module)
# print calender for a given year calendar.calender(theyear, w=0, l=0)
"""
!calendar.setfirstweekday(weekday)
Sets the weekday (0 is Monday, 6 is Sunday)
The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY are provided for convenience. 
"""
# For example, to set the first weekday to Sunday:
import calendar
print(calendar.setfirstweekday(calendar.SUNDAY))
print(calendar.firstweekday())  # Output 6

#! Get day from given year month and in format of integer 0 is monday
#! calendar.weekday(year, month, day)
print(calendar.weekday(1998, 12, 23))  # Output >>> 2


#! print day names by using 
print(list(calendar.day_name))
# >>> ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# An array that represents the days of the week in the current locale.

#! print shorthand for day names
print(list(calendar.day_abbr))
# >>> ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#! Print the month names
print(list(calendar.month_name))
# >>> ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#! Print the short months names
print(list(calendar.month_abbr))
# >>> ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#! print calender for a given year (0 is Monday) for year (1970–…), month (1–12), day (1–31).
print(calendar.calendar(2020))

#! print calender for a given year month (calendar.month(theyear, themonth, w=0, l=0))
print(calendar.month(2020, 3))

#! check months days 30/31/28/29
month_index = calendar.monthrange(2024, 2)[1]
print("Month index:", month_index)  # Output 29

# check leap year and no. of leap year in given range (calendar.isleap(year)), (calendar.leapdays(y1, y2))


##############################################################################
####################################################### # * (Datetime)
"""
date, datetime, and time objects all support a strftime(format) method,
to create a string representing the time under the control of an explicit format string.

Conversely, the datetime.strptime() class method creates a datetime object
from a string representing a date and time and a corresponding format string.
"""

#! The datetime module supplies classes for manipulating dates and times.
import datetime
#! Available Type (Objects of these types are imputable, hashable(Can be used dictionary keys),& support efficient pickling)
print(datetime.date)  # Attribute: year, month, and day. and always naive
print(datetime.time) # Attribute: hour, minute, second, microsecond, and tzinfo.
print(datetime.datetime) # Attribute: year, month, day, hour, minute, second, microsecond, and tzinfo.
print(datetime.timedelta) # Represents a duration, the difference between two datetime or date instances.
print(datetime.tzinfo)

###################################
############ (datetime) object
#! datetime objects (Is a single object containing all the information from a date "object" and a "time" object.)
# * class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
import datetime
print(datetime.datetime.today()) # 2024-03-12 12:16:13.226212 Get current date & time (no parameter req)
print(datetime.datetime.now()) # 2024-03-12 12:16:13.226212 Get current date & time (Offers more flexibility)


# Create a Datetime Object
dt = datetime.datetime(2024, 12, 11)
print(dt)  # Output 2024-12-11 00:00:00

# Get Weekday, Date and Instance attributes (read-only) Day,month,year only
current_datetime = datetime.datetime.now()
print(current_datetime.date())  # Get Date Output :2024-03-12
print(current_datetime.time())  # Get Time Output :16:30:38.210006
print(current_datetime.weekday())   # Get WeekDay Output : 1

print(current_datetime.day)     # Get Day Output :12
print(current_datetime.month)   # Get Month Output :3
print(current_datetime.year)    # Get year Output : 2024

# diff between these two datetime instance
print(datetime.date(2022, 3, 1))  # Output: 2022-03-01
print(datetime.datetime(2022, 3, 1))  # Output: 2022-03-01 00:00:00


#! classmethod datetime.strptime(date_string, format) /Get Date Output from Date String
import datetime
print(datetime.datetime.strptime("2024-12-11", "%Y-%m-%d")) # Output : 2024-12-11 00:00:00


#! classmethod datetime.strftime(format) Return a string representing the date and time, controlled by an explicit format string.
# Use strftime(format) to format the datetime object as a string
# Example :-
import datetime
formatted_date = datetime.datetime.now().strftime("%Y-%m-%d")
print(formatted_date)  # Output:2024-03-13

#! timedelta objects :-
#! datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# Example
new_date = 19/03/2020 + datetime.timedelta(days=7)    


#! classmethod datetime.fromtimestamp(timestamp, tz=None)
# Get Current DateTime based on timestamp

print(time.time())  # Output : 1710240619.0810597
print(datetime.datetime.fromtimestamp(time.time()))
# >>> 2024-03-12 16:19:34.006771

timestamp = datetime.datetime.now().timestamp()
dt = datetime.datetime.fromtimestamp(timestamp)
print(dt)  # Output: Current date and time
# >>> 2024-03-12 16:25:29.304326

"""
datetime.datetime.timetuple() and datetime.datetime.timestamp() are instance methods of datetime objects,
not class methods. Therefore, you need to create a datetime object first before calling these methods.
"""

#! datetime.timetuple() :-Return a time.struct_time such as returned by time.localtime().
print(datetime.datetime.now().timetuple())

# datetime.timetuple() is equivalent to:
# * time.struct_time((d.year, d.month, d.day, d.hour, d.minute, d.second, d.weekday(), yday, dst))
# >>> time.struct_time(tm_year=2024, tm_mon=3, tm_mday=12, tm_hour=16, tm_min=41, tm_sec=6, tm_wday=1, tm_yday=72, tm_isdst=-1)

#! datetime.timestamp()
# Return timestamp corresponding to the datetime instance. The return value is a float similar to that returned by time.time()
print(datetime.datetime.now().timestamp())
# >>> 1710241866.33591

# Instance attributes (read-only):
print(datetime.datetime.now())       # 2024-03-12 16:57:54.260399
print(datetime.datetime.now().year)  # 2024
print(datetime.datetime.now().month)  # 3
print(datetime.datetime.now().day)   # 12
print(datetime.datetime.now().hour)  # 16
print(datetime.datetime.now().minute)  # 55
print(datetime.datetime.now().second)  # 59

#! timedelta objects :-
#! datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# * A timedelta object represents a duration, the difference between two datetime or date instances.
"""
All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
Only days, seconds and microseconds are stored internally. Arguments are converted to those units:

A millisecond is converted to 1000 microseconds.
A minute is converted to 60 seconds.
An hour is converted to 3600 seconds.
A week is converted to 7 days.
"""

delta = datetime.timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta)
datetime.timedelta(days=64, seconds=29156, microseconds=10)
# >>> 64 days, 8:05:56.000010
"""
64 days: This part indicates the number of days in the timedelta.
8 hours: This part indicates the number of hours.
5 minutes: This part indicates the number of minutes.
56 seconds: This part indicates the number of seconds.
10 microseconds: This part indicates the number of microseconds.
"""


##############################
################# Date object
#! date Objects
# *A date object represents a date (year, month and day) in an idealized calendar.
# datetime.date(year, month, day) represents a date. All arguments are required. Arguments must be integers
print(datetime.date(2022, 4, 12))  # 2022-04-12

#! Return the local date
print(datetime.date.today())  # 2024-03-12

#! date.isoformat() Return a string representing the date in ISO 8601 format, YYYY-MM-DD:
print(datetime.date(2002, 12, 4).isoformat())  # '2002-12-04'

#! date.fromtimestamp(timestamp) Return the local date from given timestamp
print(datetime.date.fromtimestamp(time.time()))  # Output: 2024-03-12


#! Instance attributes (read-only):
print(datetime.date.today())       # 2024-03-12
print(datetime.date.today().year)  # 2024
print(datetime.date.today().month)  # 3
print(datetime.date.today().day)   # 12

#! date.timetuple() Return a time.struct_time such as returned by time.localtime().
print(datetime.date.today().timetuple())
# >>>> time.struct_time(tm_year=2024, tm_mon=3, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=72, tm_isdst=-1)

#! date.weekday() Returns the day of the week as an integer, where monday 0 and sunday is 6.
print(datetime.date.today().weekday())  # Output: 1 (Tuesday)

#! date.isoweekfday() Returns the day of the week as an integer, where monday is 1 and sunday is 7.
print(datetime.date.today().isoweekday())  # Output: 2 (Tuesday)


# datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
# date.replace(hour=int, minute=int, second=int)


##############################################################################
################################################# # * (Friday the 13th)
"""
Task :- 
Given the month and year as numbers, return whether that month contains a Friday 13th.
Examples :-
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False
Notes :-
January will be given as 1, February as 2, etc ...
Check Resources for some helpful tutorials on Python's datetime module.
"""
# 1st method
import datetime
def has_friday_13(month, year):
		return datetime.date(int(year), int(month), 13).weekday() == 4

# OR
def has_friday_13(month, year):
    return datetime.datetime(year, month, 13).date().weekday() == 4

# 2nd method
import datetime, calendar
def has_friday_13(month, year):
    return calendar.day_name[datetime.datetime(year, month, 13).date().weekday()] == "Friday"

# 3rd Method
def has_friday_13(month, year):
    date = f'{month} 13 {year}'.format()
    spooky = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[spooky]) == "Friday"

# 4th method
def has_friday_13(date):
    month, day, year = (int(i) for i in date.split(' '))
    spooky = datetime.date(year, month, day)
    return spooky.strftime("%A") == "Friday"

# 5th method
def has_friday_13(month, year):
    my_date = datetime.date(year, month, 13)
    return my_date.strftime("%A") == "Friday"

# 6th method
def has_friday_13(month, year):
    return calendar.weekday(year, month, 13) == 4

# %A: Represents the full name of the weekday (e.g., "Monday", "Tuesday", etc.).
# %B: Represents the full name of the month (e.g., "January", "February", etc.).
# %a: Abbreviated weekday name (e.g., "Mon", "Tue", etc.)
# %b: Abbreviated month name (e.g., "Jan", "Feb", etc.)

##############################################################################
################################################# # * (Get the Date)
"""
Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string. Each day name must be one of the following
strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".
To illustrate, the day of the week for "12/07/2016" is "Wednesday".

Examples
get_day("12/07/2016") ➞ "Wednesday"
get_day("09/04/2016") ➞ "Sunday"
get_day("12/08/2011") ➞ "Thursday"
"""
import datetime, calendar
def get_day(day):
		my_date = datetime.datetime.strptime(day, '%m/%d/%Y')
		return calendar.day_name[my_date.weekday()]

# 2nd method
import datetime
def get_day(day):
    return datetime.datetime.strptime(day, '%m/%d/%Y').strftime('%A')

# 3rd method
import time
def get_day(day):
    return time.strftime("%A", time.strptime(day, "%m/%d/%Y"))

# 4th method
from datetime import date
def get_day(day):
	m, d, y = map(int, day.split('/'))
	return date(y, m, d).strftime('%A')

# Or
import datetime
def get_day(day):
	date = day.split('/')
	m = int(date[0])
	d = int(date[1])
	y = int(date[2])
	return datetime.date(y,m,d).strftime("%A")

# 5th method
import datetime
def get_day(day):
	m,d,y = day.split('/')
	date = datetime.datetime(int(y),int(m),int(d))
	return date.strftime("%A")
# Or
import datetime, calendar
def get_day(day):
	m,d,y = day.split('/')
	date = datetime.datetime(int(y),int(m),int(d)).weekday()
	return calendar.day_name[date]


##############################################################################
################################################# # * (Unlucky Years)
"""
Create a function which returns how many Friday 13ths there are in a given year.

Examples
how_unlucky(2020) ➞ 2
how_unlucky(2026) ➞ 3
how_unlucky(2016) ➞ 1
"""
# 1st method
import datetime
def how_unlucky(y):
    count = 0
    for m in range(1, 13):
        if datetime.datetime(y, m, 13).date().weekday() == 4:
        # Or datetime.date(int(year), int(month), 13).weekday() == 4
        # Or datetime.datetime.strptime(f'{month} 13 {year}'.format(), '%m %d %Y').weekday() == 4
        # calendar.day_name[datetime.datetime(year, month, 13).date().weekday()] == "Friday"
        # datetime.date(year, month, day).strftime("%A") == "Friday"
        # calendar.weekday(year, month, 13) == 4
            count += 1
        else:
            count = count
    return count

# 2nd method
import datetime
def how_unlucky(y):
    count = 0
    for m in range(1, 13):
        if datetime.datetime(y, m, 13).date().weekday() == 4:
            count += 1
    return count

########################################################################
################################################# # * (In N Days)

"""
Task :=
If today was Monday, in two days, it would be Wednesday.
Create a function that takes in a list of days as input and the number of days to increment by. Return a list of days after n number of days has passed.

Examples
after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]
after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]
after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]
"""
# 1st method
import calendar
def after_n_days(days, n):
    my_list = list(calendar.day_name)
    my_index = [my_list.index(day) for day in days]
    print(my_index)
    result = []
    for i in my_index:   
        print((i + n) % 7)
        raw_data = my_list[(i + n) % 7]
        result.append(raw_data)
    return result
func_call = after_n_days(["Thursday", "Monday"], 4)
print(func_call)


####################################
######### Note : modulo operation
print(1%7, 2%7 ,3%7, 4%7, 5%7, 6%7, 7%7, 8%7)
# >>> 1 2 3 4 5 6 0 1

# The modulo operation is commonly used in various applications, including:
# Finding even or odd numbers (e.g., x % 2 == 0 checks if x is even).
# Cycling through a fixed range of values (e.g., day_of_week % 7 to ensure the result is within the range of 0 to 6 for days of the week).
# Hashing algorithms.
# Generating pseudo-random numbers.

def simple_hash(string):
    # Convert string to a numerical value (e.g., ASCII sum)
    hash_value = sum(ord(char) for char in string)
    # Map hash value to an index in an array of size 10 using modulo
    index = hash_value % 10
    return index

# Example usage
strings = ["apple", "banana", "orange", "grape"]
hash_table = [[] for _ in range(10)]  # Create an empty hash table of size 10
for string in strings:
    index = simple_hash(string)
    hash_table[index].append(string)
print(hash_table)

# So... now
import calendar
def after_n_days(days, n):
    my_list = list(calendar.day_name)
    my_index = [my_list.index(day) for day in days]
    print(my_index)
    result = [(my_list[(i + n) % 7]) for i in my_index]
    return result
func_call = after_n_days(["Thursday", "Monday"], 4)
print(func_call)

# So... now
import calendar
def after_n_days(days, n):
    my_list = list(calendar.day_name)
    my_index = [my_list.index(day) for day in days]
    result = [(my_list[(i + n) % 7]) for i in my_index]
    return result

# 2nd method
def afterNdays(days, n):
	weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	return [weekdays[(weekdays.index(day) + n) % 7] for day in days]

# 3rd method
import calendar 
def afterNdays(days, n):
	lst = list(calendar.day_name)
	return [lst[(lst.index(i) + n) % 7] for i in days]

########################################################################
######################################### # * (A Week Later)
"""
Create a function which takes in a date as a string, and returns the date a week after.
Examples
week_after("12/03/2020") ➞ "19/03/2020"
week_after("21/12/1989") ➞ "28/12/1989"
week_after("01/01/2000") ➞ "08/01/2000"
"""
import datetime, calendar
day_nam = list(calendar.day_name)
def week_after(d):
    my_date = datetime.datetime.strptime(d, "%d/%m/%Y").day+7
    return str(datetime.datetime.strptime(d, "%d/%m/%Y").replace(day=my_date))

# Here's correct
import datetime
def week_after(d):
    input_date = datetime.datetime.strptime(d, "%d/%m/%Y")    
    new_date = input_date + datetime.timedelta(days=7)    
    return new_date.strftime('%d/%m/%Y')

########################################################################
######################################### # * (Energy Bill Calculator)
"""
Create a function that calculates an energy bill.
Given a billing start date and end date, start and end meter reading, a unit price in pence,
and a standing charge (a daily rental fee for your meter) as arguments, calculate your bill.

An energy bill is calculated by multiplying the difference between meter readings with the unit price
and adding the number of days multiplied by the standing charge. You then have to add 5% tax.

(days between dates x standing charge) + (diference bewteen meter readings x unit price) + 5% tax

Examples
energy_bill("2020,01,01", "2020,04,01", 1000, 2000, 0.188, 0.243),  = "$220.62"
    "2020,04,01" (end date) - "2020,01,01" ( start date ),  = 91 days
    2000 ( end meter read )- 1000 ( start meter read ) = 1000 units used
    1000 (units) * 0.188p (each unit cost) = $188
    91 (days) * 0.243p (standing charge) == $22.113
    22.113 (Total standing charge cost) + $188 (total unit cost) = $210.113
    210.113 (cost) * 0.05 (uk tax on energy) = 10.50565
    210.113 (cost) + 10.50565 (tax) = 220.61865
    answer = "$220.62"
"""
# 1st method
import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    sdt = datetime.datetime.strptime(start_date, "%Y,%m,%d")
    edt = datetime.datetime.strptime(end_date, "%Y,%m,%d")
    if edt < sdt:
        return "Invalid date"
    elif start_read > end_read:
        return "Invalid meter readings"
    else:
        st_charge = (edt - sdt).days #not needed of time delta func
        meter_read = end_read - start_read
        total_unit_cost = meter_read * tariff
        stnd_charge = st_charge * stand
        return "${:.2f}".format(round((total_unit_cost + stnd_charge) + (total_unit_cost + stnd_charge) * 0.05, 2))

########################################################################
######################################### # * (Season ON earth)
"""
In this challenge, you are given a date and you have to determine the correspondent season in a certain hemisphere of Earth.
You have to use the ranges given by the meteorological seasons definition, accordingly to the following table:

Start	End	North Hemisphere	South Hemisphere
March, 1	May, 31	Spring	Autumn
June, 1	August, 31	Summer	Winter
September, 1	November, 30	Autumn	Spring
December, 1	February, 28***	Winter	Summer
Given two strings hemisphere (can be "N" for the North hemisphere or "S" for the South hemisphere) and date (name and day of the month), implement a function that returns a string with the season name, accordingly to the above table.

Examples :-
hemisphere_season("N", "June, 30") ➞ "Summer"
hemisphere_season("N", "March, 1") ➞ "Spring"
hemisphere_season("S", "September, 22") ➞ "Spring"
"""

def hemisphere_season(h, date):
	if date.split(',')[0] in ['December','January','February']:
		return 'Winter' if h == 'N' else 'Summer'
	if date.split(',')[0] in ['March','April','May']:
		return 'Spring' if h == 'N' else 'Autumn'
	if date.split(',')[0] in ['June','July','August']:
		return 'Summer' if h == 'N' else 'Winter'
	return 'Autumn' if h == 'N' else 'Spring'

def hemisphere_season(hemisphere, date):
    seasons = {
        'N': {
            'Spring': ['March', 'April', 'May'],
            'Summer': ['June', 'July', 'August'],
            'Autumn': ['September', 'October', 'November'],
            'Winter': ['December', 'January', 'February']
        },
        'S': {
            'Spring': ['September', 'October', 'November'],
            'Summer': ['December', 'January', 'February'],
            'Autumn': ['March', 'April', 'May'],
            'Winter': ['June', 'July', 'August']
        }
    }
    month = date.split(', ')[0]
    for season, months in seasons[hemisphere].items():
        if month in months:
            return season

########################################################################
###################################### # * (How Many Days Until 2021?)
"""
Given a date, return how many days date is away from 2021 (end date not included). date will be in mm/dd/yyyy format.
Examples
days_until_2021("12/28/2020") ➞ "3 days"
days_until_2021("1/1/2020") ➞ "366 days"
days_until_2021("2/28/2020") ➞ "308 days"
"""
# 1st method
import datetime
def days_until_2021(date):
    d = datetime.datetime.strptime(date, "%m/%d/%Y")  # corrected date format
    days_difference = (datetime.datetime(2021, 1, 1) - d).days
    return "{} day".format(abs(days_difference)) if abs(days_difference) == 1 else "{} days".format(abs(days_difference)) 



# 2nd method
import datetime
def days_until_2021(date):
    m = date.split("/")[0]
    Y = date.split("/")[2]
    d = date.split("/")[1]
    my_date = '/'.join([Y,m,d])
    d = datetime.datetime.strptime(my_date, "%Y/%m/%d")
    days_difference = (datetime.datetime(2021, 1, 1) - d).days
    if abs(days_difference) == 1:
        return "{} day".format(abs(days_difference)) 
    else:
        return "{} days".format(abs(days_difference)) 

# 3rd method
import datetime
def days_until_2021(date):
    m,d,Y = date.split('/')
    my_date = '/'.join((Y, m, d))
    d = datetime.datetime.strptime(my_date, "%Y/%m/%d")
    days_difference = (datetime.datetime(2021, 1, 1) - d).days
    if abs(days_difference) == 1:
        return "{} day".format(abs(days_difference)) 
    else:
        return "{} days".format(abs(days_difference))
print(days_until_2021("12/03/2020"))


########################################################################
################################################ # * (24-Hour Time?)
"""
Write a function that receives the time in 12-hour AM/PM format and returns a string representation of the time in military (24-hour) format.
Examples :-
convert_time(“07:05:45PM”) ➞ “19:05:45”
convert_time(“12:40:22AM”) ➞ “00:40:22”
convert_time(“12:45:54PM”) ➞ “12:45:54”
Notes :-
Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""
# Method
def convert_time(txt):
	from datetime import datetime
	return datetime.strptime(txt, "%I:%M:%S%p").strftime("%H:%M:%S")


########################################################################
################################################ # * (12 vs 24 Hours?)
"""
Create a function that converts 12-hour time to 24-hour time or vice versa. Return the output as a string.
Examples
convert_time("12:00 am") ➞ "0:00"
convert_time("6:20 pm") ➞ "18:20"
convert_time("21:00") ➞ "9:00 pm"
convert_time("5:05") ➞ "5:05 am"
"""
# 1st method
import datetime
def convert_time(time):
    components = time.split(" ")    
    if len(components) == 2:
        converted_time = datetime.datetime.strptime(time, "%I:%M %p").strftime("%H:%M") # wrong
    else:
        converted_time = datetime.datetime.strptime(time, "%H:%M").strftime("%-I:%M %p")
    return converted_time

# Corercted
import datetime
def convert_time(time):
    components = time.split(" ")    
    if len(components) == 2:
        converted_time = datetime.datetime.strptime(time, "%I:%M %p").strftime("%-H:%M") # wrong
    else:
        converted_time = datetime.datetime.strptime(time, "%H:%M").strftime("%-I:%M %p").lower()
    return converted_time


# 2nd method
from datetime import datetime
def convert_time(t):
	if t.endswith('m'):
		return datetime.strptime(t, '%I:%M %p').strftime('%-H:%M')
	return datetime.strptime(t, '%H:%M').strftime('%-I:%M %p').lower()


########################################################################
########################################### # * (Reformatting the Date)
"""
Create a function that converts dates from one of five string formats:

"January 9, 2019" (MM D, YYYY)
"Jan 9, 2019" (MM D, YYYY)
"01/09/2019" (MM/DD/YYYY)
"01-09-2019" (MM-DD-YYYY)
"01.09.2019" (MM.DD.YYYY)
The return value will be a list formatted like: [MM, DD, YYYY], where MM, DD, and YYYY are all integers. Using the examples above:

Examples
convert_date("January 9, 2019") ➞ [1, 9, 2019]
convert_date("Jan 9, 2019") ➞ [1, 9, 2019]
convert_date("01/09/2019") ➞ [1, 9, 2019]
convert_date("01-09-2019") ➞ [1, 9, 2019]
convert_date("01.09.2019") ➞ [1, 9, 2019]
"""
# 1st method
import datetime

def convert_date(date):
    try:
        my_date = datetime.datetime.strptime(date, "%B %d, %Y")
    except ValueError:
        try:
            my_date = datetime.datetime.strptime(date, "%b %d, %Y")
        except ValueError:
            try:
                my_date = datetime.datetime.strptime(date, "%m/%d/%Y")
            except ValueError:
                try:
                    my_date = datetime.datetime.strptime(date, "%m-%d-%Y")
                except ValueError:
                    try:
                        my_date = datetime.datetime.strptime(date, "%m.%d.%Y")
                    except ValueError:
                        return "Invalid date format"
    return [my_date.month, my_date.day, my_date.year]

# 2nd method
import datetime
import dateutil.parser
def convert_date(date):
	date = dateutil.parser.parse(date)
	return [date.month, date.day, date.year]




########################################################################
########################################### # * (Longest Streak )
"""
Create a function that takes a list of date dictionaries and return the "longest streak" (i.e. longest number of consecutive days in a row).

Example
longest_streak([
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-26"
  },
  {
    "date": "2019-09-27"
  },
  {
    "date": "2019-09-30"
  }
]) ➞ 3
"""

from datetime import datetime, timedelta
def longest_streak(lst):
	if len(lst) in [0, 1]:
		return len(lst)
	current = 1
	max_streak = 1
	for i, j in zip(lst, lst[1:]):
		t1 = datetime.strptime(i['date'],'%Y-%m-%d')
		t2 = datetime.strptime(j['date'],'%Y-%m-%d')
		if t2-t1 == timedelta(1):
			current += 1
			max_streak = max(current, max_streak)
		else:
			current = 1
	return max_streak
