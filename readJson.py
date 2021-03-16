import json

noteReplaceTarget=[[36,6,"Kick"],
              [38,12,"Snare"],
              [46,26,"HiHatOpen"],
              [49,45,"CrashLeft"],
              [57,47,"CrashRight"],
              [42,23,"HiHatClosed"],
              [48,41,"TomLow"],
              [50,38,"TomMiddle"],
              [43,41,"TomFloor"]]
noteReplace=[]

arrayLine = []
subArrayLine = []


with open("presets.txt","r") as file:

    b = 0
    for line in file:
        data = json.loads(line)
        subArrayLine.append(data['original'])
        subArrayLine.append(data['replace'])
        subArrayLine.append(data['instrument'])
        noteReplace.append(subArrayLine)
        subArrayLine = []
        b = b+1
    print(arrayLine)
    """
    data = json.load(f)
    bla = data['replace']
    print(data)"""

