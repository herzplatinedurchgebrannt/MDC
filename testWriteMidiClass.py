from writeMidiClass import WriteMidiClass

pattern=[[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
        [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]

notes = [6,12,23,44,45,46,47,48]

path = "./"
name = 'new_song1'

a = WriteMidiClass()
a.main(pattern, notes, path, name)