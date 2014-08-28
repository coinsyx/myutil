import time
import sys

if len(sys.argv) < 2:
    print('Usage: %s unix_timestamp_from_epoch' % sys.argv[0])
    exit(0)


tm = time.localtime(float(sys.argv[1]))
print( time.strftime('%Y-%m-%d %H:%M:%S', tm) )   
