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


    sequence = ["C","","D","","E","F","G","F","G","A","B","A","B","A","B"]
    bpm = 120

    def render_ui():
        ugfx.clear()
        ugfx.text(5, 5, "Sequencer", ugfx.BLACK)
        ugfx.text(5, 80, "BPM: {}".format(bpm), ugfx.BLUE)

    render_ui()

    choice = ""
    alive = True
    play = False
    while alive:
        if play:
            for note_to_play in sequence:
                if note_to_play:
                    speaker.note("{}{}".format(note_to_play, 3))
                    end_time = time.ticks_ms() + int(60/bpm*1000/4)
                    while time.ticks_ms() < end_time:
                        if is_triggered(Buttons.BTN_Menu):
                            speaker.stop()
                            alive = False
                            break
                        if is_triggered(Buttons.JOY_Up):
                            bpm += 1
                            render_ui()
                        if is_triggered(Buttons.JOY_Down):
                            bpm -= 1
                            render_ui()
                        if is_triggered(Buttons.BTN_B):
                            speaker.stop()
                            play = False
                            break
                        sleep.wfi()
                    if not play:
                        break
        if is_triggered(Buttons.BTN_A):
            play = True
        if is_triggered(Buttons.BTN_Menu):
            alive = False
        sleep.wfi()
    print("exiting")
    restart_to_default()
except Exception as e:
    speaker.stop()
    print(repr(e))
