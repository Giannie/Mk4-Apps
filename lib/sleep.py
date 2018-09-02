"""Library for sleep related functions"""

___license___ = "MIT"

import utime

def sleep_ms(duration):
    utime.sleep_ms(duration)

def sleep(duration):
    utime.sleep(duration)
