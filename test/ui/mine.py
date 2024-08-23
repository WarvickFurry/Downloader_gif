# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mine.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 606)
        MainWindow.setStyleSheet(u"QWidget {\n"
"background-color: rgb(39, 39, 42);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(100, 25))
        self.settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	padding-bottom: 2px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(39, 39, 42);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/settings_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.settings, 0, Qt.AlignmentFlag.AlignLeft)

        self.keep = QPushButton(self.centralwidget)
        self.keep.setObjectName(u"keep")
        self.keep.setMinimumSize(QSize(100, 0))
        self.keep.setSizeIncrement(QSize(137, 0))
        self.keep.setAcceptDrops(False)
        self.keep.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	padding-bottom: 2px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(39, 39, 42);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/keep_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icon/keep_off_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.keep.setIcon(icon1)
        self.keep.setCheckable(True)
        self.keep.setChecked(False)

        self.horizontalLayout_4.addWidget(self.keep, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* \u0420\u0430\u043c\u043a\u0430 \u0432\u0438\u0434\u0436\u0435\u0442\u0430 \u0441\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0430\u043c\u0438 */\n"
"     /* border-top: 2px solid rgb(85, 123, 226); */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 6px; /* \u0441\u0434\u0432\u0438\u0433\u0430\u0435\u043c \u0432\u043f\u0440\u0430\u0432\u043e \u043d\u0430 5px */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(39, 39, 42);\n"
"    min-width: 80px;\n"
"	min-height: 10px;\n"
"    padding: 2px;\n"
"    border-right: 0px solid rgb(85, 123, 226);\n"
"	border-top: 2px solid rgb(85, 123, 226);\n"
"	border-left: 1px solid rgb(85, 123, 226);\n"
"	border-bottom: 2px solid rgb(85, 123, 226);\n"
"	border-right: 1px solid rgb(85, 123, 226);\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    border-right: 0px solid rgb(85, 123, 226);\n"
"	border-top-left-radius: 3px;\n"
"	border-top: 2px solid rgb(85, 123, 226);\n"
"	border-left: 2px solid rgb(85, 123, 226);\n"
"	borde"
                        "r-bottom: 2px solid rgb(85, 123, 226);\n"
"	border-right: 1px solid rgb(85, 123, 226);\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left: 0px solid rgb(85, 123, 226);\n"
"	border-top-right-radius: 3px;\n"
"	border-top: 2px solid rgb(85, 123, 226);\n"
"	border-right: 2px solid rgb(85, 123, 226);\n"
"	border-left: 1px solid rgb(85, 123, 226);\n"
"	border-bottom: 2px solid rgb(85, 123, 226);\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* \u043f\u0435\u0440\u0432\u0430\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043f\u0435\u0440\u0435\u043a\u0440\u044b\u0432\u0430\u0435\u0442 \u0441\u043b\u0435\u0432\u0430 \u043e\u0442 \u0441\u0435\u0431\u044f */\n"
"	border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u0432\u043a\u043b\u0430"
                        "\u0434\u043a\u0430 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043f\u0435\u0440\u0435\u043a\u0440\u044b\u0432\u0430\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430 \u043e\u0442 \u0441\u0435\u0431\u044f */\n"
"	border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* \u0434\u0435\u043b\u0430\u0435\u043c \u043d\u0435\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 \u043c\u0435\u043d\u044c\u0448\u0435 */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgba(85, 123, 226, 130);\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.backgroud = QWidget(self.tab)
        self.backgroud.setObjectName(u"backgroud")
        self.gridLayout = QGridLayout(self.backgroud)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(72, -1, 30, -1)
        self.lineEdit_ = QLineEdit(self.backgroud)
        self.lineEdit_.setObjectName(u"lineEdit_")
        self.lineEdit_.setMinimumSize(QSize(606, 41))
        self.lineEdit_.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 16pt \"Segoe UI\";\n"
"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	padding-bottom: 5px;\n"
"	max-width: 1000px;\n"
"	min-width: 600px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(39, 39, 42);\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgba(85, 123, 226, 250);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.lineEdit_, 0, Qt.AlignmentFlag.AlignBottom)

        self.download_button = QPushButton(self.backgroud)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	height: 30px;\n"
"	width: 130px;\n"
"	max-height: 30px;\n"
"	max-width: 130px;\n"
"	min-height: 30px;\n"
"	min-width: 130px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/download_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download_button.setIcon(icon2)
        self.download_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.download_button, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalWidget = QWidget(self.backgroud)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(660, 101))
        self.gridLayout_8 = QGridLayout(self.horizontalWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setContentsMargins(30, 0, 30, 42)
        self.progressBar = QProgressBar(self.horizontalWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(600, 30))
        self.progressBar.setMaximumSize(QSize(16777215, 30))
        self.progressBar.setSizeIncrement(QSize(600, 30))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"     border: 3px solid rgb(85, 123, 226);\n"
"     border-radius: 8px;\n"
"     text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.323864 rgba(60, 143, 241, 255), stop:1 rgba(0, 81, 224, 255));\n"
"	border-radius: 4px;\n"
"	\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.gridLayout_8.addWidget(self.progressBar, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label = QLabel(self.horizontalWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.label, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_4.addWidget(self.horizontalWidget, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.backgroud, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 0, 0, 0)
        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"	border: 0px solid rgb(85, 123, 226);\n"
"")
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 12, 6)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridWidget = QWidget(self.tab_3)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.gridWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.webEngineView = QWebEngineView(self.gridWidget)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy1.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy1)
        self.webEngineView.setMinimumSize(QSize(600, 291))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout.addWidget(self.webEngineView)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.test_pushButton = QPushButton(self.gridWidget)
        self.test_pushButton.setObjectName(u"test_pushButton")
        self.test_pushButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.test_pushButton.sizePolicy().hasHeightForWidth())
        self.test_pushButton.setSizePolicy(sizePolicy2)
        self.test_pushButton.setMinimumSize(QSize(172, 35))
        self.test_pushButton.setMaximumSize(QSize(172, 35))
        self.test_pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/folder_open_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.test_pushButton.setIcon(icon3)
        self.test_pushButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.test_pushButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.text_autTags = QTextEdit(self.gridWidget)
        self.text_autTags.setObjectName(u"text_autTags")
        self.text_autTags.setMinimumSize(QSize(350, 0))
        self.text_autTags.setMaximumSize(QSize(350, 16777215))
        self.text_autTags.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.text_autTags.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.text_autTags.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.text_autTags.setTabStopDistance(1000.000000000000000)

        self.gridLayout_2.addWidget(self.text_autTags, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.gridWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(824, 81))
        self.widget.setMaximumSize(QSize(16777215, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 20, 1, 20)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.set_date = QDateEdit(self.widget)
        self.set_date.setObjectName(u"set_date")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.set_date.sizePolicy().hasHeightForWidth())
        self.set_date.setSizePolicy(sizePolicy3)
        self.set_date.setMinimumSize(QSize(111, 25))
        self.set_date.setMaximumSize(QSize(102, 25))
        self.set_date.setSizeIncrement(QSize(0, 0))
        self.set_date.setMouseTracking(True)
        self.set_date.setStyleSheet(u"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    background-color: rgb(39, 39, 42); /* \u041e\u0431\u044b\u0447\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 (\u0431\u0435\u043b\u044b\u0439) */\n"
"	alternate-background-color: rgb(39, 39, 42);\n"
"    color: #FFFFFF; /* \u041e\u0431\u044b\u0447\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 (\u0447\u0435\u0440\u043d\u044b\u0439) */\n"
"}\n"
"QDateTimeEdit {\n"
"	 min-width: 105px;\n"
"    border: 3px solid rgb(85, 123, 226); \n"
"}\n"
"QDateTimeEdit QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(:/icon/arrow_circle_left_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg); /* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u043d\u0430\u0437\u0430\u0434 */\n"
"    width: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    "
                        "height: 30px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"QDateTimeEdit QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(:/icon/arrow_circle_right_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg); /* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0432\u043f\u0435\u0440\u0435\u0434 */\n"
"    width: 30px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    height: 30px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"")
        self.set_date.setAccelerated(True)
        self.set_date.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.set_date)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.put_aside_pushButton = QPushButton(self.widget)
        self.put_aside_pushButton.setObjectName(u"put_aside_pushButton")
        self.put_aside_pushButton.setMinimumSize(QSize(146, 41))
        self.put_aside_pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	height: 30px;\n"
"	width: 130px;\n"
"	max-height: 30px;\n"
"	max-width: 130px;\n"
"	min-height: 30px;\n"
"	min-width: 130px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/publish_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.put_aside_pushButton.setIcon(icon4)
        self.put_aside_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.put_aside_pushButton, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.set_time = QComboBox(self.widget)
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.addItem("")
        self.set_time.setObjectName(u"set_time")
        self.set_time.setMinimumSize(QSize(99, 30))
        self.set_time.setMaximumSize(QSize(99, 30))
        self.set_time.setStyleSheet(u"\n"
"QComboBox {\n"
"border: 3px solid rgb(85, 123, 226); \n"
"font: 14pt \"Segoe UI\";\n"
"}")
        self.set_time.setEditable(True)
        self.set_time.setFrame(True)

        self.horizontalLayout_2.addWidget(self.set_time)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget)


        self.gridLayout_6.addWidget(self.gridWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0435\u0440 \u0413\u0438\u0432\u043e\u043a", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433\u0438", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.keep.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0435\u043f\u0438\u0442\u044c", None))
        self.lineEdit_.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430  \u0434\u0435\u0440\u043f\u0438\u0431\u0443\u0440\u0443", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c gif", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u0427\u0442\u043e\u0431 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0433\u0438\u0444\u043a\u0443 \u043d\u0443\u0436\u043d\u043e:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">1. \u0412 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a"
                        "\u0430\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430 \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f (\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u2192 \u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430: \u0412\u043a\u043b\u044e\u0447\u0435\u043d\u044b)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">2. \u0412 \u0433\u0440\u0430\u0444\u0435 (\u0440\u0430\u0431\u043e\u0442\u0430 \u0441 AIP) \u0441\u043e\u0437\u0434\u0430\u0451\u043c \u043a\u043b\u044e\u0447 \u0441\u043e \u0432\u0441\u0435\u043c\u0438 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u044f\u043c\u0438, \u0434\u0430\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447 \u0432 \u0432\u043e\u0434\u0438\u043c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0432"
                        " \u0440\u0430\u0437\u0434\u0435\u043b (\u0432\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">3. \u0412 \u0433\u0440\u0430\u0444\u0435 (\u0440\u0430\u0437\u0434\u0435\u043b\u044b) \u0432\u043a\u043b\u044e\u0447\u0430\u0435\u043c \u0444\u0430\u0439\u043b\u044b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u043d\u0430 \u044d\u0442\u043e\u043c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/WarvickFurry/Downloader_gif.git\"><span style=\" font-size:12pt; text-decoration: underline; color:#297acc;\">GitHub</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.test_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.text_autTags.setDocumentTitle("")
        self.text_autTags.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u043c\u044b\u0445 \u0442\u0435\u0433\u043e\u0432", None))
        self.put_aside_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None))
        self.set_time.setItemText(0, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.set_time.setItemText(1, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.set_time.setItemText(2, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.set_time.setItemText(3, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.set_time.setItemText(4, QCoreApplication.translate("MainWindow", u"19:00", None))
        self.set_time.setItemText(5, QCoreApplication.translate("MainWindow", u"21:00", None))
        self.set_time.setItemText(6, QCoreApplication.translate("MainWindow", u"23:00", None))
        self.set_time.setItemText(7, QCoreApplication.translate("MainWindow", u"01:00", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0438\u043d\u0433", None))
    # retranslateUi

