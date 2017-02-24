import datetime

date_start = '01-02-2013'
date_stop = '07-28-2015'
new_start = datetime.datetime.strptime(date_start, "%m-%d-%Y")
new_end = datetime.datetime.strptime(date_stop, "%m-%d-%Y")
print new_end - new_start

date_start = '12312013'  
date_stop = '05282015'
new_start = datetime.datetime.strptime(date_start, "%m%d%Y")
new_end = datetime.datetime.strptime(date_stop, "%m%d%Y")
print new_end - new_start

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
new_start = datetime.datetime.strptime(date_start, "%d-%b-%Y")
new_end = datetime.datetime.strptime(date_stop, "%d-%b-%Y")
print new_end - new_start