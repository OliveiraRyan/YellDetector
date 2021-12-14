import sounddevice as sd
import numpy as np
import os
import sys
import math
import time
import datetime
import argparse

from timeit import default_timer as timer

parser = argparse.ArgumentParser(description="Beeps at you when you\'re too loud", 
                                 formatter_class=argparse.RawTextHelpFormatter)
# needs to be renamed and able to set to a choice of low/med/high or something similar
# e.g. -s (sensitivity), -l (level)
parser.add_argument("-vol", "--volume", help="normalized volume value that triggers a 'yell'",
                    type=int, default=180)
parser.add_argument("-d", "--duration", type=int, default=1,
                    help="time (in seconds) in between 'yells' (default 1 second)")
parser.add_argument("-v", "--verbosity", type=int, default=0, choices=[0,1,2], 
                    help="""how verbose the program is:
    0 = no printed output
    1 = outputs audio bars
    2 = outputs normalized volume values""")
parser.add_argument("-nr", "--NoRecord", help="disables recording data into a .csv file", action="store_true")

args = parser.parse_args()

# normalized volume value that triggers a 'yell' (Default 180)
volume = args.volume

# Duration in seconds between 'yells' (Default 1 second)
duration = args.duration

# Determines the verbosity of the printed output
# 0 = no output, 1 = bars, 2 = exact values
verbosity = args.verbosity

# In Powershell, this creates the windows noise 
cmd = "echo " + chr(7)


yell_counter = 0
start_time = timer()

# Save for later!!! -- grabs and formats current datetime. Used for storing time of yell in .csv
# current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_sound(indata, outdata, frames, time, status):
    global yell_counter
    volume_norm = np.linalg.norm(indata)*10

    if (verbosity == 1):
        print ("|" * int(volume_norm))
    elif (verbosity == 2):
        print(int(volume_norm))

    if (volume_norm >= volume): # 180 seems like a good start
        os.system(cmd)
        yell_counter += 1
        sd.sleep(duration * 1000)

try: 
    with sd.Stream(blocksize=0, callback=print_sound):
        # sd.sleep(duration * 1000)
        print('press Ctrl+C to stop the recording')
        while True:
            time.sleep(60)

except KeyboardInterrupt:
    seconds = math.trunc(timer() - start_time)
    # formats elapsed time in seconds to datetime format, accounting for rollover (>24h)
    elapsed_time = str(datetime.timedelta(seconds=seconds))

    if (args.NoRecord):
        sys.exit('Interrupted by user. Program ran for {}'.format(elapsed_time))
    sys.exit('Interrupted by user; you yelled {} times within a time interval of {}!'.format(yell_counter, elapsed_time))