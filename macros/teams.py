# MS Teams Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'MS Teams', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio', [Keycode.COMMAND, Keycode.SHIFT, Keycode.M]),
        (0x000754, 'Chat', [Keycode.COMMAND, 2]),
        (0x04541B, 'Video', [Keycode.COMMAND, Keycode.SHIFT, Keycode.O]),
        # 2nd row ----------
        (0x002000, 'Share', [Keycode.COMMAND, Keycode.SHIFT, Keycode.E]),
        (0x000000, "", []),
        (0x000000, "", []),
        # 3rd row ----------
        (0x000040, 'Lt On', [Keycode.COMMAND, Keycode.F2]),
        (0x004000, 'Cam Set', [Keycode.OPTION, '1', -Keycode.OPTION, Keycode.OPTION, 't']),
        (0x000040, 'Lt Off', [Keycode.COMMAND, Keycode.F1]),
        # 4th row ----------
        (0x200000, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x080F54, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}# Write your code here :-)
