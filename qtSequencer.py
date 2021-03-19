import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from writeMidiClass import WriteMidiClass

class EigenerEvent(QObject):
    schliessmichEvent = pyqtSignal()

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        #self.write_File = WriteMidiClass()

        self.pattern=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.notes = [6,12,23,44,45,46,47,48]

        self.sig = EigenerEvent()
        self.sig.schliessmichEvent.connect(self.close)

        self.setGeometry(400,600,650,500)
        self.setWindowTitle("Qt Drum Sequencer")
        self.setWindowIcon(QIcon("coconut.png"))

        self.statusBar().showMessage("Das ist eine Status Bar")

        exitMe = QAction(QIcon('coconut.png'), '&Close', self)
        exitMe.setShortcut('Ctrl+E')
        exitMe.setStatusTip('Exit')
        exitMe.triggered.connect(self.close)

        saveMidi = QAction(QIcon('coconut.png'), 'Save', self)
        saveMidi.triggered.connect(self.saveMidi)

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction("Open")
        file.addAction(saveMidi)
        file.addSeparator()
        file.addAction(exitMe)
        view = menubar.addMenu('&View')

        

        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exitMe)
        
        QToolTip.setFont(QFont('Arial',14))
        
        play_button = QPushButton('Play', self)
        play_button.setObjectName("Play")
        play_button.move(70,340)
        play_button.setToolTip('Play <b>Sequencer</b>')
        play_button.clicked.connect(self.gedrueckt)

        stop_button = QPushButton('Stop', self)
        stop_button.setObjectName("Stop")
        stop_button.move(175,340)
        stop_button.setToolTip('Stop <b>Sequencer</b>')

        self.button_list = []
        start_in_x = 70
        start_in_y = 50
        distance = 35

        x = start_in_x
        y = start_in_y
        for i in range (0,8):
            for j in range(0,16):
                self.button = QPushButton(str(j+1), self)
                self.button.move(x,y)
                self.button.setToolTip('Set <b>note</b>')
                self.button.setObjectName(str(i)+"_"+str(j))
                self.button.setMaximumWidth(30)
                self.button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
                self.button_list.append(self.button)
                self.button.pressed.connect(self.gedrueckt)
                x = x + distance
            x = start_in_x
            y = y + distance

        self.onlyInt = QIntValidator()
        y = start_in_y
        for k in range(0,8):
            self.w = QLineEdit(self)
            self.w.move(25,y)
            self.w.setMaximumWidth(30)
            self.w.setText(str(self.notes[k]))
            self.w.setAlignment(Qt.AlignCenter)
            self.w.setStyleSheet('QLineEdit {background-color: #A3C1DA; color: gray;}')
            self.w.setValidator(self.onlyInt)
            self.w.setMaxLength(3)
            y = y + distance

        self.show()

    def gedrueckt(self):
        sender = self.sender()
        a = sender.objectName().split("_")

        if self.pattern[int(a[0])][int(a[1])]==0:
            self.pattern[int(a[0])][int(a[1])] = 1
            sender.setStyleSheet('QPushButton {background-color: gray; color: red;}')
        else:
            self.pattern[int(a[0])][int(a[1])] = 0
            sender.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
        print(self.pattern)

    def saveMidi(self):
        writeFile = WriteMidiClass
        writeFile.writeMidi(self, self.pattern, self.notes, "./", "bla")

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_E:
            self.sig.schliessmichEvent.emit()
"""
    def writeMidi (self):
        self.write_File.writeMidi(self.pattern, self.notes, "./", "bla")"""


app = QApplication(sys.argv)
w = Fenster()

sys.exit(app.exec_())
