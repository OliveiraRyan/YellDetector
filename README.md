# YellDetector

## **Important Note:**  
Currently only works on Windows in PowerShell

## Instructions:
The script will run continuously until a keyboard interrupt (Ctrl+C) is issued.

Currently, the normalized input volume will be printed in the terminal. If the value is over 200, a Windows Noise will play.

## Useful links:
* [Sounddevice docs](https://python-sounddevice.readthedocs.io/en/0.4.3/)

## TODO:
* Make printing of input volume be a parse command (default: off)
* Make the value that a windows noise is made be customizable
* Log the yells!
  * Probably into a CSV
* Make the script Linux compatible
  * Possibly a Linux version
* Clean up the code so it isn't just a straight script
  * i.e. `if __name__ == "__main__"`