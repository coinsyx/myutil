import time
import sys


def print_usage_info():
    print('Usage:  %s day' % sys.argv[0])
    print('Example:  %s  2014-02-04' % sys.argv[0])


if len(sys.argv) != 2:
    print_usage_info()
    exit(0)


date = sys.argv[1]
if len(date) != 10:
    print_usage_info()
    exit(0)

tup = date.split('-')
if len(tup) != 3 or len(tup[0]) != 4 or len(tup[1]) != 2 or len(tup[2]) != 2:
    print_usage_info()
    exit(0)

time_str_start = date + ' 00:00:00'

ts = time.strptime(time_str_start, '%Y-%m-%d %H:%M:%S')
time_unix_start = time.mktime(ts)
time_unix_end = time_unix_start + 86400

print('unix_epoch_start: %.0f' % time_unix_start)
print('unix_epoch_end: %.0f' % time_unix_end)



