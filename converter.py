import os
import sys
import json
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from mido import Message,MidiFile,MidiTrack
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox

# class stuff work in progress
class PathFiles:
    def __init__(self, bla):
        if bla == "midi":
            self.midi_list('./grooves/')
        elif bla == "preset":
            self.preset_list('./presets/')

    def midi_list(self, path):
        self.pathm = path
        self.folders = os.listdir(path)
        self.a = 0
        for self.foldm in self.folders:
            if not ".mid" in self.foldm:
                self.folders.remove(self.foldm)
                self.a = self.a+1
        #print(self.folders)

    def preset_list(self, path):
        self.pathp = path
        self.folders = os.listdir(path)
        self.a = 0
        for self.foldp in self.folders:
            if not ".txt" in self.foldp:
                self.folders.remove(self.foldp)
                self.a = self.a+1
        print(self.folders)

preset_files = PathFiles("preset")
midi_files = PathFiles("midi")

# [[before][after][instrument]],...
"""
noteReplace= [[36,6,"Kick"],
              [38,12,"Snare"],
              [46,26,"HiHatOpen"],
              [49,45,"CrashLeft"],
              [57,47,"CrashRight"],
              [42,23,"HiHatClosed"],
              [48,41,"TomLow"],
              [50,38,"TomMiddle"],
              [43,41,"TomFloor"]]"""

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("lx Midi Converter")
        self.setStyleSheet("background-color: #E5FFCC;") 

        self.ui.convert.clicked.connect(self.convert_files)
        self.ui.convert.setStyleSheet("background-color: yellow;")
        self.ui.actionMidi_Folder.triggered.connect(self.open_folder_midi)
        self.ui.actionPreset_Folder.triggered.connect(self.open_preset_folder)
        self.ui.actionClose.triggered.connect(lambda:self.close())

        x = 0
        y = 0
        for midi_file in midi_files.folders:
            self.ui.listFiles.insertItem(x, midi_file)
        for preset_file in preset_files.folders:
            self.ui.comboBox.insertItem(y, preset_file)   

    def open_folder_midi(self):
        if self.ui.checkBox.checkState()== 2:
            print("rekursiv")
        else: 
            print("nicht rekursiv")
        self.ui.listFiles.clear()
        fold = QFileDialog.getExistingDirectory(self, "Select midi folder...")
        if not fold[-1] == "/":
            fold = fold+"/"
        midi_files.midi_list(fold)
        x = 0
        for midi_file in midi_files.folders:
            if ".mid" in midi_file:
                self.ui.listFiles.insertItem(x, midi_file)

    def open_preset_folder(self):
        self.ui.comboBox.clear()
        fold = QFileDialog.getExistingDirectory(self, "Select preset folder...")
        if not fold[-1] == "/":
            fold = fold+"/"
        preset_files.preset_list(fold)
        y = 0
        for preset_file in preset_files.folders:
            self.ui.comboBox.insertItem(y, preset_file)   

    def convert_files(self):
        select = self.ui.comboBox.currentText()
        extension = self.ui.extension.text()

        #selectedPreset = self.ui.listPresets.currentItem().text()
        result_in_box = []
        subresult = []
        try:
            with open("./presets/"+select,"r") as file:
                subArrayLine = []
                noteReplace = []
                b = 0
                for line in file:
                    data = json.loads(line)
                    subArrayLine.append(data['original'])
                    subArrayLine.append(data['replace'])
                    subArrayLine.append(data['instrument'])
                    noteReplace.append(subArrayLine)
                    subArrayLine = []
                    b = b+1     
            for midi_file in midi_files.folders:
                if ".mid" in midi_file:
                    subresult.append(midi_file)
                    check_mod_exist = midi_file.replace(".mid",extension+".mid")
                    if not "_mod.mid" in midi_file and not check_mod_exist in midi_files.folders:
                        mid = MidiFile(midi_files.pathm + midi_file)
                        for i, track in enumerate(mid.tracks):
                            for msg in track:
                                if "note_on" in str(msg):
                                    x = 0
                                    for pups in noteReplace:
                                        if msg.note == noteReplace[x][0]:
                                            msg.note = noteReplace[x][1]
                                            break
                                        x = x+1
                        name_new = mid.filename.replace(".mid",extension+".mid")
                        mid.save(name_new)
                        subresult.append("Converted")
                        #print("Created new MIDI file: "+ name_new)
                    else:
                        #print("done nothing")
                        subresult.append("Done nothing")
                        pass
                    result_in_box.append(subresult)
                    subresult = []
            print(result_in_box)

            #bla = QMessageBox.about(self, "tite", result_in_box.
        except FileNotFoundError():
            print("file not found")

window = MainWindow()
window.show()

sys.exit(app.exec_())


