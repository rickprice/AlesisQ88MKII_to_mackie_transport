# process.py - shows how to process MIDI events in Python
#
# This is a curious little script that inverts the velocity of note-on events.
# The harder you press the keys, the quieter the sound will become :)
#
# Events on channels other than channel 1 are discarded.
#

from mididings import *

config(
    client_name='Q88 Transport to Mackie',
)

remap_list = { 9 : 11}

def convert_to_mackie(ev):
    if ev.channel == 1:
        if ev.note in remap_list: 
            ev.note = remap_list[ev.note]
        return ev
    else:
        return ev


run(Process(convert_to_mackie))

