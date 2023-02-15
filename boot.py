import board
import digitalio
import displayio
import storage
import usb_cdc
import usb_midi

from time import sleep

b1 = digitalio.DigitalInOut(board.KEY1)
b1.switch_to_input(pull=digitalio.Pull.UP)

if not b1.value:
    print("Dev mode.\nMounting drive...")
else:
    print("Normal mode.\nDisabling drive...")
    usb_cdc.disable()
    storage.disable_usb_drive()

usb_midi.disable()