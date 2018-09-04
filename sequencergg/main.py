"""Sequencer
v0.4
"""

___name___         = "Sequencer"
___license___      = "MIT"
___categories___   = ["Sound"]
___dependencies___ = ["speaker", "buttons", "ugfx_helper", "app"]

try:
    import ugfx, speaker, ugfx_helper, sleep, time
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

    render_ui()

    choice = ""
    alive = True
    while alive:
        for note_to_play in sequence:
            if note_to_play:
                speaker.note("{}{}".format(note_to_play, 3))
                end_time = time.ticks_ms() + int(60/bpm*1000)
                while time.ticks_ms() < end_time:
                    if is_triggered(Buttons.BTN_Menu):
                        speaker.stop()
                        alive = False
                    if is_triggered(Buttons.JOY_Up):
                        bpm += 1
                    if is_triggered(Buttons.JOY_Down):
                        bpm -= 1
                    if is_triggered(Buttons.BTN_A):
                        speaker.stop()
                    sleep.wfi()

    restart_to_default()
except Exception as e:
    speaker.stop()
    print(repr(e))
