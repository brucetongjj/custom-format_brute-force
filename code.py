import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize USB keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Button setup - using D5 and D6 as requested
button_start = digitalio.DigitalInOut(board.D5)   # Start button on D5
button_start.direction = digitalio.Direction.INPUT
button_start.pull = digitalio.Pull.UP

button_stop = digitalio.DigitalInOut(board.D6)    # Stop button on D6
button_stop.direction = digitalio.Direction.INPUT
button_stop.pull = digitalio.Pull.UP

print("XIAO RP2040 Brute-Forcer ready!")
print("Press button on D5 to START typing")
print("Press button on D6 to STOP at any time")
time.sleep(1)

def is_pressed(btn):
    return not btn.value  # Active-low because of Pull.UP

running = False

while True:
    # Check for Start button (D5)
    if is_pressed(button_start) and not running:
        print("START pressed on D5 - beginning to type all codes...")
        running = True
        time.sleep(0.4)  # debounce

    # Main typing loop - only runs when running is True
    if running:
        for num in range(100):                    # 00 to 99
            if not running:
                break
            num_str = f"{num:02d}"
            
            for a in "abcdefghijklmnopqrstuvwxyz":
                if not running: break
                for b in "abcdefghijklmnopqrstuvwxyz":
                    if not running: break
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if not running: break
                        
                        code = num_str + a + b + c
                        layout.write(code + "\n")
                        time.sleep(0.05)   # Adjust this: smaller = faster, larger = slower

        if running:
            print("Finished all combinations!")
        else:
            print("Stopped by button on D6.")
        running = False
        time.sleep(0.5)

    # Check for Stop button (D6) even when idle
    if is_pressed(button_stop) and running:
        running = False
        print("STOP pressed on D6!")
        time.sleep(0.3)

    time.sleep(0.01)  # Small delay to keep the board responsive