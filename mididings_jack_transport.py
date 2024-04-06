from mididings import *
import jack

jack.attach('blah')

def jackStart(ev):
    jack.transport_start()

def jackStop(ev):
    jack.transport_stop()

def jackRewind(ev):
    jack.transport_locate(0)

startCC = 117
stopCC = 116
rewindCC = 116

run( [ CtrlFilter(startCC) >> Process(jackStart),
       CtrlFilter(stopCC) >> Process(jackStop),
       CtrlFilter(rewindCC) >> Process(jackRewind)] )
