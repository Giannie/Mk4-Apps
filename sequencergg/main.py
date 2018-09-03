"""Sequencer
Fixed button ref 0.2
"""

___name___         = "Sequencer"
___license___      = "MIT"
___categories___   = ["Sound"]
___dependencies___ = ["speaker", "buttons", "ugfx_helper", "app"]

import ugfx, speaker, ugfx_helper
from tilda import Buttons
from buttons import *
from app import restart_to_default
import utime

sequence = ["C","","D","","E","","F","","G","","A","","B","","C"]
bpm = 120

def render_ui():
    ugfx.clear()
    ugfx.text(5, 5, "Sequencer", ugfx.BLACK)
    ugfx.text(5, 80, "BPM: {}".format(bpm), ugfx.BLUE)

while True:
    for note_to_play in sequence:
        if is_pressed(Buttons.BTN_Menu):
            break
        if note_to_play:
            speaker.note("{}{}".format(note_to_play, 3))
            utime.sleep_ms(500)

restart_to_default()
