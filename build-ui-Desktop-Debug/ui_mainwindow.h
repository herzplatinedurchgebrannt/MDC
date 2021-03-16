/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSpeichern;
    QAction *actionMidi_Folder;
    QAction *actionPreset_Folder;
    QAction *actionDefault;
    QAction *actionClose;
    QAction *actionOpen_Midi_Folder;
    QWidget *centralwidget;
    QFormLayout *formLayout;
    QTabWidget *tabWidget;
    QWidget *tab;
    QGridLayout *gridLayout;
    QListWidget *listFiles;
    QComboBox *comboBox;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label;
    QLineEdit *extension;
    QPushButton *convert;
    QCheckBox *checkBox;
    QWidget *tab_2;
    QMenuBar *menubar;
    QMenu *menu1;
    QMenu *menu2;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(500, 608);
        actionSpeichern = new QAction(MainWindow);
        actionSpeichern->setObjectName(QString::fromUtf8("actionSpeichern"));
        actionMidi_Folder = new QAction(MainWindow);
        actionMidi_Folder->setObjectName(QString::fromUtf8("actionMidi_Folder"));
        actionPreset_Folder = new QAction(MainWindow);
        actionPreset_Folder->setObjectName(QString::fromUtf8("actionPreset_Folder"));
        actionDefault = new QAction(MainWindow);
        actionDefault->setObjectName(QString::fromUtf8("actionDefault"));
        actionClose = new QAction(MainWindow);
        actionClose->setObjectName(QString::fromUtf8("actionClose"));
        actionOpen_Midi_Folder = new QAction(MainWindow);
        actionOpen_Midi_Folder->setObjectName(QString::fromUtf8("actionOpen_Midi_Folder"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        formLayout = new QFormLayout(centralwidget);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        gridLayout = new QGridLayout(tab);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        listFiles = new QListWidget(tab);
        listFiles->setObjectName(QString::fromUtf8("listFiles"));

        gridLayout->addWidget(listFiles, 0, 1, 1, 1);

        comboBox = new QComboBox(tab);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        gridLayout->addWidget(comboBox, 2, 1, 1, 1);

        label_2 = new QLabel(tab);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setLayoutDirection(Qt::LeftToRight);
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_2, 2, 0, 1, 1);

        label_3 = new QLabel(tab);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_3, 3, 0, 1, 1);

        label = new QLabel(tab);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        extension = new QLineEdit(tab);
        extension->setObjectName(QString::fromUtf8("extension"));

        gridLayout->addWidget(extension, 3, 1, 1, 1);

        convert = new QPushButton(tab);
        convert->setObjectName(QString::fromUtf8("convert"));

        gridLayout->addWidget(convert, 4, 1, 1, 1);

        checkBox = new QCheckBox(tab);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));

        gridLayout->addWidget(checkBox, 1, 1, 1, 1);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        tabWidget->addTab(tab_2, QString());

        formLayout->setWidget(0, QFormLayout::FieldRole, tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 500, 22));
        menu1 = new QMenu(menubar);
        menu1->setObjectName(QString::fromUtf8("menu1"));
        menu2 = new QMenu(menubar);
        menu2->setObjectName(QString::fromUtf8("menu2"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menu1->menuAction());
        menubar->addAction(menu2->menuAction());
        menu1->addSeparator();
        menu1->addAction(actionMidi_Folder);
        menu1->addAction(actionPreset_Folder);
        menu1->addSeparator();
        menu1->addAction(actionClose);
        menu2->addAction(actionOpen_Midi_Folder);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSpeichern->setText(QCoreApplication::translate("MainWindow", "Action", nullptr));
        actionMidi_Folder->setText(QCoreApplication::translate("MainWindow", "Midi Folder", nullptr));
        actionPreset_Folder->setText(QCoreApplication::translate("MainWindow", "Preset Folder", nullptr));
        actionDefault->setText(QCoreApplication::translate("MainWindow", "Default", nullptr));
        actionClose->setText(QCoreApplication::translate("MainWindow", "Close", nullptr));
        actionOpen_Midi_Folder->setText(QCoreApplication::translate("MainWindow", "Open Midi Folder", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Preset", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Extension", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Midi Files", nullptr));
        extension->setText(QCoreApplication::translate("MainWindow", "_mod", nullptr));
        convert->setText(QCoreApplication::translate("MainWindow", "Convert Files", nullptr));
        checkBox->setText(QCoreApplication::translate("MainWindow", "Rekursiv", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "Convert", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("MainWindow", "Files", nullptr));
        menu1->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menu2->setTitle(QCoreApplication::translate("MainWindow", "View", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
