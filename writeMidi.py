from mido import Message, MidiFile, MidiTrack, MetaMessage
from mido import bpm2tempo
import numpy as np

mid = MidiFile()
track0 = MidiTrack()
track1 = MidiTrack()
mid.tracks.append(track0)
mid.tracks.append(track1)

#track.append(Message('program_change', program=12, time=0))
mytempo = bpm2tempo(120)
print(mytempo)

track0.append(MetaMessage('track_name', name='master', time = 0))
track0.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
track0.append(MetaMessage('set_tempo',tempo = mytempo, time = 0))

#430 passt zu 120bpm, time = 50
#190
delta = 70

pattern=[1,1,1,1]

pattern2=[[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
          [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
          [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
          [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
          [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
          [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
          [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]

# get number of lines + rows of pattern
a = np.array(pattern2)

note = [6,12,23,44,45,46,47,48]

isPlaying = [False,False,False,False]

track1.append(MetaMessage('track_name', name='Inst 1', time = 0))
track1.append(MetaMessage('instrument_name', name='DrumGizmo', time = 0))
track1.append(Message('control_change', channel=0,control=0,value=0,time=0))
track1.append(Message('control_change', channel=0,control=32,value=0,time=0))
track1.append(Message('program_change', channel=0,program=0,time=0))
track1.append(Message('control_change', channel=0,control=32,value=0,time=0))

firstNote = True

# first run, start at 0s
for i in range(0,a.shape[0]):
    if pattern2[i][0] == 1:
        track1.append(Message('note_on', note=note[i], velocity=127, time=0))
        
for i in range(0,a.shape[0]):
    if pattern2[i][0] == 1:
        if firstNote == True:
            track1.append(Message('note_off', note=note[i], velocity=0, time=50))
            firstNote = False
        else:
            track1.append(Message('note_off', note=note[i], velocity=0, time=0))

# loop for the rest
for j in range(1,a.shape[1]):
    firstNote = True
    for i in range(0,a.shape[0]):
        if pattern2[i][j] == 1:
            if firstNote == True:
                track1.append(Message('note_on', note=note[i], velocity=127, time=delta))
                firstNote = False
            else:
                track1.append(Message('note_on', note=note[i], velocity=127, time=0))
    firstNote = True
    for i in range(0,a.shape[0]):
        if pattern2[i][j] == 1:
            if firstNote == True:
                track1.append(Message('note_off', note=note[i], velocity=0, time=50))
                firstNote = False
            else:
                track1.append(Message('note_off', note=note[i], velocity=0, time=0))

mid.save('new_song5.mid')