# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.listFiles = QtWidgets.QListWidget(self.tab)
        self.listFiles.setObjectName("listFiles")
        self.gridLayout.addWidget(self.listFiles, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.extension = QtWidgets.QLineEdit(self.tab)
        self.extension.setObjectName("extension")
        self.gridLayout.addWidget(self.extension, 3, 1, 1, 1)
        self.convert = QtWidgets.QPushButton(self.tab)
        self.convert.setObjectName("convert")
        self.gridLayout.addWidget(self.convert, 4, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionMidi_Folder = QtWidgets.QAction(MainWindow)
        self.actionMidi_Folder.setObjectName("actionMidi_Folder")
        self.actionPreset_Folder = QtWidgets.QAction(MainWindow)
        self.actionPreset_Folder.setObjectName("actionPreset_Folder")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_Midi_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Midi_Folder.setObjectName("actionOpen_Midi_Folder")
        self.menu1.addSeparator()
        self.menu1.addAction(self.actionMidi_Folder)
        self.menu1.addAction(self.actionPreset_Folder)
        self.menu1.addSeparator()
        self.menu1.addAction(self.actionClose)
        self.menu2.addAction(self.actionOpen_Midi_Folder)
        self.menubar.addAction(self.menu1.menuAction())
        self.menubar.addAction(self.menu2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Preset"))
        self.label_3.setText(_translate("MainWindow", "Extension"))
        self.label.setText(_translate("MainWindow", "Midi Files"))
        self.extension.setText(_translate("MainWindow", "_mod"))
        self.convert.setText(_translate("MainWindow", "Convert Files"))
        self.checkBox.setText(_translate("MainWindow", "Rekursiv"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Files"))
        self.menu1.setTitle(_translate("MainWindow", "File"))
        self.menu2.setTitle(_translate("MainWindow", "View"))
        self.actionSpeichern.setText(_translate("MainWindow", "Action"))
        self.actionMidi_Folder.setText(_translate("MainWindow", "Midi Folder"))
        self.actionPreset_Folder.setText(_translate("MainWindow", "Preset Folder"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionOpen_Midi_Folder.setText(_translate("MainWindow", "Open Midi Folder"))
