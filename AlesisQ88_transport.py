#! /usr/bin/env python3
# Convert Alesis Q88 MKII transport codes to more correct Mackie control codes
#
# Set your Q88 keyboard to Mackie Control mode by pressing "Advanced" and then
# The "DAW"" white key  until the LEDs below "Advanced" are green. Then press the 
# "Enter" white key.

from mididings import *

config(
    client_name = 'Q88 Mackie Transport',
    # backend = 'jack',
    in_ports = [('in','Q88 MKII:.*Transport.*')],
    out_ports = [('Transport')]

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

