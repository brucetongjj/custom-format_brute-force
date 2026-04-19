# V3 - Mirror Branching Brute-Forcer
Default starting code: 50aaa (true middle of 00-99 and aaa-zzz)
## Features
Starts from the middle (50aaa) by default and branches outwards symmetrically.
Supports full mirror branching for both numbers and letters.
When you start from a specific code (e.g. 48zzz), it begins exactly there, then goes to its mirror, and continues branching outwards.
Keeps the slow 0.4 second delay between each submission as requested.
## Button Controls
D5 → Start brute force (mirror branching outwards from current code)
D6 → Stop typing immediately
D7 → Previous position (cycle left through the 5 characters)
D9 → Next position (cycle right through the 5 characters)
D8 → Decrease the character at current position (down)
D10 → Increase the character at current position (up)
# Update Instructions
Replace main.py currently on the device to the updated main.py included in the releases.
# First time setup
##### Note - this setup uses a seeed studio XIAO-RP2040, other devices are not guaranteed to work
## Step 1: Install CircuitPython on the XIAO RP2040
Download the latest stable CircuitPython UF2 for your board:
https://circuitpython.org/board/seeeduino_xiao_rp2040/
(Get the .uf2 file named something like adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.1.4.uf2 — version 10.x is fine.)
Put the board into bootloader mode:
Press and hold the BOOT button (the button labeled “B” on the board).
While still holding it, plug the XIAO into your computer with a USB-C cable.
A drive called RP1-RP2 will appear.

Drag-and-drop the downloaded .uf2 file onto the RP1-RP2 drive.
The drive will disconnect and re-appear as CIRCUITPY. Installation is complete.

## Step 2: Install the adafruit_hid library (required for keyboard emulation)
Download the CircuitPython Library Bundle that matches your CircuitPython version (10.x):
https://circuitpython.org/libraries
→ Choose the 10.x mpy bundle (the big zip file, e.g. adafruit-circuitpython-bundle-10.x-mpy-YYYYMMDD.zip).
Unzip the bundle.
Inside the unzipped folder you will find a lib folder.
Copy the entire adafruit_hid folder from the bundle’s lib folder into the lib folder on your CIRCUITPY drive.
(Create the lib folder on CIRCUITPY if it doesn’t exist.)

## Step 3: Add the code
On the CIRCUITPY drive, replace the file code.py with the code published in the releases.
