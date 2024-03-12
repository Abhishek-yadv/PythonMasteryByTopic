####################################################################
########################################################## (Dates)
####################################################################

##########################################################
####################################### (time module)
#! sleep() function:
# time.sleep(seconds): Suspends program execution for the specified duration (in seconds).
# Useful for introducing delays or pausing program execution. For instance:
import time
for i in range(4):
    time.sleep(1)
    print(i)

#! time() Function: - 
# time.time(): Returns the current time in seconds since the epoch (January 1, 1970) a floating point number.
# It's platform-dependent and useful for measuring execution time or generating timestamps.
import time
current_time = time.time()
print(f"Current time in seconds since epoch: {current_time:.6f}")
# >>> Current time in seconds since epoch: 1710163167.377825

#! (Converting a Time Object to a String)
#! strftime(format, tuple): stands for “string format time.
# format strings from a given time objet struct_time/Python time tuple
time.strftime('%Y-%m-%d', time.localtime())
# >>> '2019-03-01'


#! asctime()
# You use asctime() for converting a time tuple or struct_time to a timestamp:
print(time.asctime(time.gmtime()))  # Output : Mon Mar 11 13:49:05 2024
print(time.asctime(time.localtime()))  # Output: Mon Mar 11 19:19:30 2024


#! Converting a String to an time Object(struct_time) :
#! strptime :
"""
To convert a time string to a struct_time, you use strptime(), which stands for “string parse time”
Or (Converts a string representation of a date or time into a date or time object or struct_time object.)
"""
print(time.strptime('2019-03-01', '%Y-%m-%d'))
# >>> time.struct_time(tm_year=2019, tm_mon=3, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=60, tm_isdst=-1)

#? Both gmtime() and localtime() return struct_time instances, for UTC and local time respectively.
import time
print(time.gmtime())
print(time.localtime())
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=11, tm_hour=13, tm_min=54, tm_sec=17, tm_wday=0, tm_yday=71, tm_isdst=0)
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=11, tm_hour=19, tm_min=24, tm_sec=17, tm_wday=0, tm_yday=71, tm_isdst=0)


#! ctime([secs]) Functions:
# time.ctime(): Converts a specified timestamp into a human-readable date and time format
# Or Getting time string from seconds, If no argument is passed, it calculates the time till the present.
import time
timestamp = 1627908313.717886
formatted_time = time.ctime(timestamp)
print(f"Current time: {formatted_time}")
# >>> Current time: Mon Aug  2 18:15:13 2021 <str>


timestamp = 1627908313.717886
formatted_time = time.ctime([23234])

"""
# If secs is not provided or None, the current time as returned by time() is used.
# ctime(secs) is equivalent to asctime(localtime(secs)). Locale information is not used by ctime().
"""

import time
current_time = time.ctime(time.time())
print(current_time)
# >>> Mon Mar 11 19:12:50 2024 #str

import time
my_lctime = time.asctime((time.localtime()))
print(my_lctime)
my_ctime = time.ctime()
print(my_ctime)
# >>> Tue Mar 12 08:39:16 2024
# >>> Tue Mar 12 08:39:16 2024

#! time.gmtime(0): 
# Retrieves the time in the GMT (Greenwich Mean Time) timezone at the Unix epoch) (January 1, 1970, 00:00:00 UTC).
import time
epoch_time = time.gmtime(0)
print(f"Epoch time: {epoch_time}")
# >>> Epoch time: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

import time
epoch_time = time.gmtime()
print(f"Epoch time: {epoch_time}")
# >>> Epoch time: time.struct_time(tm_year=2024, tm_mon=3, tm_mday=12, tm_hour=2, tm_min=59, tm_sec=48, tm_wday=1, tm_yday=72, tm_isdst=0)

#! time.localtime():
# time.localtime(): Returns a named tuple representing local time (non-epochal timestamps). You can access its values by both index and attribute name.
import time
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
import time
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
###################################### (calender module)
# print calender for a given year calendar.calender(theyear, w=0, l=0)
"""
!calendar.setfirstweekday(weekday)
Sets the weekday (0 is Monday, 6 is Sunday) to start each week. 
The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY are provided for convenience. 
"""
# For example, to set the first weekday to Sunday:

# Returns the current setting for the weekday to start each week.
import calendar
print(calendar.setfirstweekday(calendar.SUNDAY))
print(calendar.firstweekday()) # Output 6

#! Get day from given year month and in format of integer 0 is monday
#! calendar.weekday(year, month, day)
import calendar
print(calendar.weekday(1998, 12, 23))  # Output >>> 2


#! print day names by using calender.day_name(An array that represents the days of the week in the current locale.)
import calendar
print(list(calendar.day_name))
# >>> ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# An array that represents the days of the week in the current locale.

#! print shorthand for day names
import calendar
print(list(calendar.day_abbr))
# >>> ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#! Print the month names
import calendar
print(list(calendar.month_name))
# >>> ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#! Print the short months names
import calendar
print(list(calendar.month_abbr))
# >>> ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#! print calender for a given year (0 is Monday) for year (1970–…), month (1–12), day (1–31).
print(calendar.calendar(2020))

#! print calender for a given year month (calendar.month(theyear, themonth, w=0, l=0))
print(calendar.month(2020, 3))

#! check months days 30/31/28/29
import calendar
month_index = calendar.monthrange(2024, 2)[1]
print("Month index:", month_index) #Output 29

# check leap year or not (calendar.isleap(year))
# Check no. of leap year (calendar.leapdays(y1, y2))

##############################################################################
################################################### #* (Datetime)
#! The datetime module supplies classes for manipulating dates and times.
#! Available Type 
import datetime
print(datetime.date)     #Attribute: year, month, and day. and always naive
print(datetime.time)     #Attribute: hour, minute, second, microsecond, and tzinfo.
print(datetime.datetime) #Attribute: year, month, day, hour, minute, second, microsecond, and tzinfo.
print(datetime.timedelta)#Represents a duration, the difference between two datetime or date instances.
print(datetime.tzinfo)
#! Objects of these types are imputable, hashable(Can be used dictionary keys), support efficient pickling via the pickle module.

################### (datetime)
#! datetime objects (Is a single object containing all the information from a date object and a time object.)
#* class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
import datetime
print(datetime.datetime.today()) # 2024-03-12 12:16:13.226212 Get current date & time (no parameter req)
print(datetime.datetime.now())   # 2024-03-12 12:16:13.226212 Get current date & time (Offers more flexibility)


# Get Weekday, Date and Instance attributes (read-only)Day,month,year only
import datetime
current_datetime = datetime.datetime.now()
print(current_datetime.date())  # Get Date Output :2024-03-12
print(current_datetime.time())  # Get Time Output :16:30:38.210006
print(current_datetime.weekday())   # Get WeekDay Output : 1

print(current_datetime.day)     # Get Day Output :12
print(current_datetime.month)   # Get Month Output :3
print(current_datetime.year)    # Get year Output : 2024

#! classmethod datetime.strptime(date_string, format) /Get Date Output from Date String
import datetime
print(datetime.datetime.strptime("2024-12-11", "%Y-%m-%d")) #Output : 2024-12-11 00:00:00


#! classmethod datetime.strftime(date_string, format) Return a string representing the date and time, controlled by an explicit format string.
import datetime
# Create a datetime object
dt = datetime.datetime(2024, 12, 11)

# Use strftime() to format the datetime object as a string
formatted_date = dt.strftime("%Y-%B-%d")
print(formatted_date) # Output:2024-December-11

#! classmethod datetime.fromtimestamp(timestamp, tz=None) 
# Get Current DateTime based on timestamp
import time, datetime
print(time.time())  # Output : 1710240619.0810597
print(datetime.datetime.fromtimestamp(time.time())) #Get Current DateTime based on timestamp
# >>> 2024-03-12 16:19:34.006771

import datetime
timestamp = datetime.datetime.now().timestamp()
dt = datetime.datetime.fromtimestamp(timestamp)
print(dt)  # Output: Current date and time
# >>> 2024-03-12 16:25:29.304326


#! classmethod date.fromisoformat(date_string)
# Return a date corresponding to a date_string given in any valid ISO 8601 format, with the following exceptions:
import datetime
print(datetime.date.fromisoformat('2019-12-04')) #2019-12-04
print(datetime.date.fromisoformat('20191204'))   #2019-12-04

import datetime
print(datetime.date.fromisocalendar(2019, 3, 2))

"""
datetime.datetime.timetuple() and datetime.datetime.timestamp() are instance methods of datetime objects,
not class methods. Therefore, you need to create a datetime object first before calling these methods.
"""

#! datetime.timetuple() :-Return a time.struct_time such as returned by time.localtime().
import datetime
print(datetime.datetime.now().timetuple())
# datetime.timetuple() is equivalent to:
#* time.struct_time((d.year, d.month, d.day, d.hour, d.minute, d.second, d.weekday(), yday, dst))
# >>> time.struct_time(tm_year=2024, tm_mon=3, tm_mday=12, tm_hour=16, tm_min=41, tm_sec=6, tm_wday=1, tm_yday=72, tm_isdst=-1)

#! datetime.timestamp()
# Return timestamp corresponding to the datetime instance. The return value is a float similar to that returned by time.time()
import datetime
print(datetime.datetime.now().timestamp())
#>>> 1710241866.33591

# Instance attributes (read-only):
import datetime
print(datetime.datetime.now())       # 2024-03-12 16:57:54.260399
print(datetime.datetime.now().year)  # 2024
print(datetime.datetime.now().month) # 3
print(datetime.datetime.now().day)   # 12
print(datetime.datetime.now().hour)  # 16
print(datetime.datetime.now().minute)# 55
print(datetime.datetime.now().second)# 59

#! datetime.timetuple() :-Return a time.struct_time such as returned by time.localtime().

#! timedelta objects :- 
#! datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#* A timedelta object represents a duration, the difference between two datetime or date instances.
"""
All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
Only days, seconds and microseconds are stored internally. Arguments are converted to those units:

A millisecond is converted to 1000 microseconds.
A minute is converted to 60 seconds.
An hour is converted to 3600 seconds.
A week is converted to 7 days.
"""

import datetime
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


#################### date object
#! date Objects
# *A date object represents a date (year, month and day) in an idealized calendar.
# datetime.date(year, month, day) represents a date. All arguments are required. Arguments must be integers
import datetime
print(datetime.date(2022, 4, 12))  # 2022-04-12

#! Return the local date
print(datetime.date.today())  # 2024-03-12

#! date.isoformat() Return a string representing the date in ISO 8601 format, YYYY-MM-DD:
import datetime
print(datetime.date(2002, 12, 4).isoformat())  # '2002-12-04'

#! date.fromtimestamp(timestamp) Return the local date from given timestamp
import datetime, time
print(datetime.date.fromtimestamp(time.time()))  # Output: 2024-03-12

#! date.fromisoformat(date_string) return the local date from given string
from datetime import date
print(date.fromisoformat('2019-12-04'))  # Output: 2019-12-04

#! date.fromisocalendar(year, week, day)
from datetime import date
print(date.fromisocalendar(2024, 3, 2))  # Output: 2024-01-16

#! Instance attributes (read-only):
import datetime
print(datetime.date.today())       # 2024-03-12
print(datetime.date.today().year)  # 2024
print(datetime.date.today().month) # 3
print(datetime.date.today().day)   # 12

#! date.timetuple() Return a time.struct_time such as returned by time.localtime().
import datetime
print(datetime.date.today().timetuple())
#! time.struct_time(tm_year=2024, tm_mon=3, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=72, tm_isdst=-1)

#! date.weekday() Returns the day of the week as an integer, where monday 0 and sunday is 6.
import datetime
print(datetime.date.today().weekday())  # Output: 1 (Tuesday)

#! date.isoweekfday() Returns the day of the week as an integer, where monday is 1 and sunday is 7.
import datetime
print(datetime.date.today().isoweekday())  # Output: 2 (Tuesday)

#! date.isocalendar() Return a named tuple object with three components: year, week and weekday.
import datetime
print(datetime.date.today().isocalendar()) #Output: datetime.IsoCalendarDate(year=2024, week=11, weekday=2)

################################
######### time Objects
# A time object represents a (local) time of day, independent of any particular day, and subject to adjustment via a tzinfo object
#! time.fromisoformat(time_string)
# Return a time froma time_string in any valid ISO 8601 format, 
from datetime import time
print(time.fromisoformat('04:23:01'))  # Ouptut : 04:23:01


#! time.isoformat(timespec='auto')
# Return a string representing the time in ISO 8601 format, one of:
from datetime import time
# Create a time object
my_time = time(4, 23, 1)
# Use isoformat() method to get ISO formatted string
print(type(my_time.isoformat())) 



##############################################################################
################################################### #* (Friday the 13th)
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
# Method 1
import datetime
import calendar
def has_friday_13(month, year):
    date = f'{month} 13 {year}'.format()
    spooky = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[spooky]) == "Friday"

# 2nd method
import datetime
def has_friday_13(date):
    month, day, year = (int(i) for i in date.split(' '))   
    spooky = datetime.date(year, month, day) 
    return spooky.strftime("%A") == "Friday"

# 3rd method
import datetime
def has_friday_13(month, year):
    spooky = datetime.date(year, month, 13)
    return spooky.strftime("%A") == "Friday"

# Or
def has_friday_13(month, year):
    return datetime.date(year, month, 13).strftime("%A") == "Friday"




