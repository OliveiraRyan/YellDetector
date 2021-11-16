# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np
import os
import sys
import time
# In Powershell, this creates the windows noise 
cmd = "echo " + chr(7)

# Duration in seconds
# duration = 10

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    # print ("|" * int(volume_norm))
    print(int(volume_norm))
    if (volume_norm >= 200):
        os.system(cmd)
        # sys.exit(0)

try: 
    with sd.Stream(callback=print_sound):
        # sd.sleep(duration * 1000)
        # print('press Ctrl+C to stop the recording')
        while True:
            time.sleep(60)

except KeyboardInterrupt:
    sys.exit('Interrupted by user')