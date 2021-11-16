# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np
import os
import sys
import time
# In Powershell, this creates the windows noise 
cmd = "echo " + chr(7)

# Duration in seconds between 'yells'
duration = 1

yell_counter = 0

def print_sound(indata, outdata, frames, time, status):
    global yell_counter
    volume_norm = np.linalg.norm(indata)*10

    # print ("|" * int(volume_norm))
    # print(int(volume_norm))

    if (volume_norm >= 50): # 180 seems like a good start
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
    sys.exit('Interrupted by user, you yelled {} times'.format(yell_counter))