from mido import MidiFile


path = './grooves/'

mid = MidiFile('master2.mid')

#mid = MidiFile('new_song.mid')


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)


print("///////////////////////////////")

mid = MidiFile('new_song5.mid')

#mid = MidiFile('new_song.mid')


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)