# process.py - shows how to process MIDI events in Python
#
# This is a curious little script that inverts the velocity of note-on events.
# The harder you press the keys, the quieter the sound will become :)
#
# Events on channels other than channel 1 are discarded.
#

from mididings import *

config(
    client_name = 'Q88 Mackie Transport',
    # backend = 'jack',
    in_ports = [('in','Q88 MKII:.*Transport.*')],
    out_ports = [('out')]

)

# Stop, Play, Record all seem to work correctly already
remap_notes = { 
    # Cursor Up
    96 : 84,
    # Cursor Down
    97 : 85,
    # Scrub Button
    100 : 86,
    # Cursor Left
    98 : 88,
    # Cursor Right
    99 : 89,
    }

def convert_to_mackie(ev):
    # If we match, then alter the note
    if ev.channel == 1:
        if ev.type in (NOTEON,NOTEOFF):
            if ev.note in remap_notes: 
                ev.note = remap_notes[ev.note]
    return ev

run(Process(convert_to_mackie))

