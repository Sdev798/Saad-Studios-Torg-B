# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-global-1vETUVj.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 794)
        MainWindow.setMinimumSize(QSize(1100, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_4 = QGridLayout(self.tab1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.watermark = QLabel(self.tab1)
        self.watermark.setObjectName(u"watermark")
        self.watermark.setStyleSheet(u"font: 10pt \"Poppins\";")
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.watermark, 4, 0, 1, 1)

        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1039, 658))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.nw_task = QPushButton(self.tab1)
        self.nw_task.setObjectName(u"nw_task")
        self.nw_task.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.nw_task, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 2, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_13 = QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(10, 0))
        self.pushButton.setStyleSheet(u"font: 14pt \"Poppins\";")

        self.horizontalLayout.addWidget(self.pushButton)

        self.startpomo = QPushButton(self.frame)
        self.startpomo.setObjectName(u"startpomo")
        sizePolicy.setHeightForWidth(self.startpomo.sizePolicy().hasHeightForWidth())
        self.startpomo.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.startpomo.setFont(font1)
        self.startpomo.setStyleSheet(u"")
        self.startpomo.setCheckable(True)

        self.horizontalLayout.addWidget(self.startpomo)

        self.settingpomo = QPushButton(self.frame)
        self.settingpomo.setObjectName(u"settingpomo")
        sizePolicy.setHeightForWidth(self.settingpomo.sizePolicy().hasHeightForWidth())
        self.settingpomo.setSizePolicy(sizePolicy)
        self.settingpomo.setMinimumSize(QSize(189, 54))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.settingpomo.setFont(font2)
        self.settingpomo.setStyleSheet(u"")
        self.settingpomo.setIconSize(QSize(32, 32))
        self.settingpomo.setCheckable(False)

        self.horizontalLayout.addWidget(self.settingpomo)


        self.gridLayout_7.addWidget(self.frame, 2, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(700, 200))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(72)
        font3.setWeight(QFont.Light)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel{\n"
"	border-radius:10px;\n"
"	border:3px solid rgb(185, 23, 26);\n"
"	font: 300 72pt \"Poppins\";\n"
"\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(15)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_2, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_12 = QGridLayout(self.tab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.webEngineView = QWebEngineView(self.tab)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"https://www.youtube.com/"))

        self.gridLayout_12.addWidget(self.webEngineView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_19 = QGridLayout(self.page_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_21 = QGridLayout(self.groupBox_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_20.addWidget(self.label_3, 4, 0, 1, 1)

        self.addtask = QPushButton(self.groupBox_2)
        self.addtask.setObjectName(u"addtask")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(12)
        font5.setWeight(QFont.DemiBold)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.addtask.setFont(font5)
        self.addtask.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(83, 54, 252);\n"
"	padding:10px;\n"
"	font: 600 12pt \"Poppins\";\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(82, 106, 226);\n"
"\n"
"}")

        self.gridLayout_20.addWidget(self.addtask, 2, 0, 1, 1)

        self.checkbuttontext = QLineEdit(self.groupBox_2)
        self.checkbuttontext.setObjectName(u"checkbuttontext")

        self.gridLayout_20.addWidget(self.checkbuttontext, 1, 0, 1, 1)

        self.sswebsite = QCommandLinkButton(self.groupBox_2)
        self.sswebsite.setObjectName(u"sswebsite")
        self.sswebsite.setDefault(False)

        self.gridLayout_20.addWidget(self.sswebsite, 5, 0, 1, 1)

        self.taskname_add = QLineEdit(self.groupBox_2)
        self.taskname_add.setObjectName(u"taskname_add")
        self.taskname_add.setStyleSheet(u"font: 16pt \"Poppins\";\n"
"padding:20px;")

        self.gridLayout_20.addWidget(self.taskname_add, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_16 = QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_11.addWidget(self.pushButton_3, 9, 0, 1, 1)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 0, 4);")

        self.gridLayout_11.addWidget(self.label_6, 6, 0, 1, 1)

        self.password_line = QLineEdit(self.page_3)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setStyleSheet(u"font: 10pt \"Poppins\";")
        self.password_line.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_11.addWidget(self.password_line, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.showpass = QCheckBox(self.page_3)
        self.showpass.setObjectName(u"showpass")
        self.showpass.setStyleSheet(u"font: 11pt \"Poppins\";")

        self.gridLayout_11.addWidget(self.showpass, 7, 0, 1, 1)

        self.notename = QLineEdit(self.page_3)
        self.notename.setObjectName(u"notename")

        self.gridLayout_11.addWidget(self.notename, 3, 0, 1, 1)

        self.set_password_button = QPushButton(self.page_3)
        self.set_password_button.setObjectName(u"set_password_button")
        self.set_password_button.setStyleSheet(u"font: 11pt \"Poppins\";")

        self.gridLayout_11.addWidget(self.set_password_button, 8, 0, 1, 1)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line, 1, 0, 1, 1)

        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_2, 12, 0, 1, 1)

        self.company_watermark = QLabel(self.page_3)
        self.company_watermark.setObjectName(u"company_watermark")
        self.company_watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.company_watermark, 13, 0, 1, 1)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 10pt \"Poppins\";")

        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 1)

        self.security_watermark = QLabel(self.page_3)
        self.security_watermark.setObjectName(u"security_watermark")
        self.security_watermark.setStyleSheet(u"font: 28pt \"Poppins\";")
        self.security_watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.security_watermark, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_24 = QGridLayout(self.page_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.showpassword_m = QCheckBox(self.page_4)
        self.showpassword_m.setObjectName(u"showpassword_m")

        self.gridLayout_23.addWidget(self.showpassword_m, 5, 1, 1, 1)

        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font:34pt \"Poppins\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_8, 0, 1, 1, 1)

        self.set_master_password = QPushButton(self.page_4)
        self.set_master_password.setObjectName(u"set_master_password")
        self.set_master_password.setStyleSheet(u"font: 16pt \"Poppins\";")

        self.gridLayout_23.addWidget(self.set_master_password, 7, 1, 1, 1)

        self.password_master_password = QLineEdit(self.page_4)
        self.password_master_password.setObjectName(u"password_master_password")
        self.password_master_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_master_password.setClearButtonEnabled(True)

        self.gridLayout_23.addWidget(self.password_master_password, 4, 1, 1, 1)

        self.remenber_password = QCheckBox(self.page_4)
        self.remenber_password.setObjectName(u"remenber_password")

        self.gridLayout_23.addWidget(self.remenber_password, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_3, 9, 1, 1, 1)

        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 900 15pt \"Poppins\";")

        self.gridLayout_23.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 14pt \"Poppins\";")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_9, 10, 1, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.watermark.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Technology Co, LTD / Saad Studios Torg V1.1 Beta Global", None))
        self.nw_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Task Managment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.startpomo.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.settingpomo.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pomodoro Timer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simplicity is our goal if you want many features Create your app Now by Visiting Our Website", None))
        self.addtask.setText(QCoreApplication.translate("MainWindow", u"Add New Task", None))
        self.checkbuttontext.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Check Button text", None))
        self.sswebsite.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Website", None))
        self.taskname_add.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Set The Master Password as a Passphrase for this Note", None))
        self.label_6.setText("")
        self.password_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.showpass.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.notename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Note Name", None))
        self.set_password_button.setText(QCoreApplication.translate("MainWindow", u"Set Password", None))
        self.company_watermark.setText(QCoreApplication.translate("MainWindow", u"Secured By Saad Studios Security / Saad Studios Technology Co, LTD / Saad Studios Torg V1.2.2 Alpha", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Please Set Your Password For Protect Your Note", None))
        self.security_watermark.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Security", None))
        self.showpassword_m.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Security", None))
        self.set_master_password.setText(QCoreApplication.translate("MainWindow", u"Set Master Password", None))
        self.password_master_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Master Password", None))
        self.remenber_password.setText(QCoreApplication.translate("MainWindow", u"Remember Password ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dear User,\n"
"Your Security  is Very Important\n"
"Please Set You Master Password For Protect Your Notes ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Secured By Saad Studios Security / Saad Studios Technology Co, LTD / Saad Studios Torg 1.2", None))
    # retranslateUi

