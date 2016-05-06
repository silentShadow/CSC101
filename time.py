'''\
Rev: 1
Author: SilentShadow
Description: displaying dates and times
Reference: Listing 2.12
Page: 46 (PDF 66)
'''

import time

curr_time = time.time()         # Current time
all_secs  = int( curr_time )    # Seconds since midnight 01 Jan 1970
curr_sec  = all_secs % 60       # Grab current second
all_mins  = all_secs // 60      # Grab total minutes
curr_min  = all_mins % 60       # Current minute of the hour
all_hrs   = all_mins // 60      # Grab total hours
curr_hr   = all_hrs % 24        # Grab current hour


print( "Current time is {}:{}:{} GMT".format( curr_hr, curr_min, curr_min ) )