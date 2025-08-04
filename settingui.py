# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsuiMTACZv.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(433, 186)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.setokbutton = QPushButton(self.centralwidget)
        self.setokbutton.setObjectName(u"setokbutton")

        self.gridLayout_2.addWidget(self.setokbutton, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.focus = QComboBox(self.centralwidget)
        self.focus.setObjectName(u"focus")
        self.focus.setEditable(True)

        self.gridLayout.addWidget(self.focus, 0, 1, 1, 1)

        self.breaktimecombo = QComboBox(self.centralwidget)
        self.breaktimecombo.setObjectName(u"breaktimecombo")
        self.breaktimecombo.setEditable(True)

        self.gridLayout.addWidget(self.breaktimecombo, 1, 1, 1, 1)

        self.longbreakcombo = QComboBox(self.centralwidget)
        self.longbreakcombo.setObjectName(u"longbreakcombo")
        self.longbreakcombo.setEditable(True)

        self.gridLayout.addWidget(self.longbreakcombo, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.setokbutton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Long Break TIme", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Short Break Time", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Focus Time", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Technology Co., LTD / Saad Studios Torg 1.1 Beta Global", None))
    # retranslateUi

