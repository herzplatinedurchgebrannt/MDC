import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

"""
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
        name = 'new_song10'
        """

class EigenerEvent(QObject):
    schliessmichEvent = pyqtSignal()

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
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

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction("Open")
        file.addAction("Save")
        file.addSeparator()
        file.addAction(exitMe)
        view = menubar.addMenu('&View')

        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exitMe)
        
        QToolTip.setFont(QFont('Arial',14))
        
        play_button = QPushButton('Play', self)
        play_button.setObjectName("Play")
        play_button.move(100,400)
        play_button.setToolTip('Play <b>Sequencer</b>')
        play_button.clicked.connect(self.gedrueckt)

        stop_button = QPushButton('Stop', self)
        stop_button.setObjectName("Stop")
        stop_button.move(400,400)
        stop_button.setToolTip('Stop <b>Sequencer</b>')

        #print(stop_button.text())

        distance = 35

        #self.button_layout = QHBoxLayout()
        #self.widget_layout = QVBoxLayout()

        self.button_list = []

        start_in_x = 50
        start_in_y = 50

        x = start_in_x
        y = start_in_y
        for i in range (0,8):
            for j in range(0,16):
                self.button = QPushButton(str(j+1), self)
                self.button.move(x,y)
                self.button.setToolTip('Set <b>note</b>')
                self.button.setObjectName(str(i)+"_"+str(j))
                self.button.setMaximumWidth(30)
                self.button_list.append(self.button)
                self.button.pressed.connect(self.gedrueckt)
                #self.button.pressed.connect(self.gedrueckt)
                x = x + distance
            x = start_in_x
            y = y + distance
        self.show()

    def gedrueckt(self):
        sender = self.sender()
        pressed_button = sender.objectName().split("_")
        print(pressed_button)

        sender.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        
        #print(sender.objectName())

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_E:
            self.sig.schliessmichEvent.emit()

app = QApplication(sys.argv)
w = Fenster()

sys.exit(app.exec_())