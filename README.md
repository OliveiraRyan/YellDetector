# YellDetector

## **Important Note:**  
Currently only works on Windows in PowerShell

## Instructions:
The script will run continuously until a keyboard interrupt (Ctrl+C) is issued.

Currently, the normalized input volume will be printed in the terminal. If the value is over 200, a Windows Noise will play.

### Optional Arguments

-h, --help &mdash; show this help message and exit  
-vol, --volume &mdash; normalized volume value that triggers a 'yell'  
-v {0,1,2}, --verbosity {0,1,2} &mdash; how verbose the program is:
* 0 = no printed output
* 1 = outputs audio bars
* 2 = outputs normalized volume values

-d, --duration &mdash; time (in seconds) in between 'yells' (default 1 second)  
-nr, --NoRecord &mdash; disables recording data into a .csv file

## Useful links:
* [Sounddevice docs](https://python-sounddevice.readthedocs.io/en/0.4.3/)

## TODO:
* ~~Make printing of input volume be a parse command (default: off)~~
* Make the volume level that triggers a 'yell' made be customizable
  * ~~Make it a parse command~~
  * Set levels instead of a specified number (e.g. low/med/high)
  * Also give option to set a specific number
* Log the yells!
  * Probably into a CSV
* Make the script Linux compatible
  * Possibly a Linux version
* Clean up the code so it isn't just a straight script
  * i.e. `if __name__ == "__main__"`