# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog_settings(object):
    def setupUi(self, Dialog_settings):
        if not Dialog_settings.objectName():
            Dialog_settings.setObjectName(u"Dialog_settings")
        Dialog_settings.resize(698, 461)
        Dialog_settings.setStyleSheet(u"QWidget {\n"
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
"	padding-right: 8;\n"
"	padding-left: 8;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(Dialog_settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Dialog_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
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
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_12 = QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(15, -1, 9, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(380, 16777215))
        self.scrollArea.setStyleSheet(u"	border: 0px solid rgb(85, 123, 226);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 412))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.auto_swap_tab_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.auto_swap_tab_checkBox.setObjectName(u"auto_swap_tab_checkBox")
        self.auto_swap_tab_checkBox.setMaximumSize(QSize(360, 16777215))
        self.auto_swap_tab_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_8.addWidget(self.auto_swap_tab_checkBox)

        self.auto_swap_time_data_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.auto_swap_time_data_checkBox.setObjectName(u"auto_swap_time_data_checkBox")
        self.auto_swap_time_data_checkBox.setMaximumSize(QSize(360, 16777215))
        self.auto_swap_time_data_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_8.addWidget(self.auto_swap_time_data_checkBox)

        self.blur_token_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.blur_token_checkBox.setObjectName(u"blur_token_checkBox")
        self.blur_token_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_8.addWidget(self.blur_token_checkBox)

        self.verticalGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMaximumSize(QSize(360, 16777215))
        self.verticalGroupBox.setStyleSheet(u"\n"
" QGroupBox {\n"
"\n"
"	 color: rgb(255, 255, 255);\n"
"   	 border: 3px solid rgb(85, 123, 226);\n"
"	 border-radius: 6px;\n"
"	 font: 700 10pt \"Segoe UI\";\n"
"     margin-top: 1ex; /* \u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e \u0432\u0432\u0435\u0440\u0445\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
" }\n"
" QGroupBox::title {\n"
"	left: 6px;\n"
"	border-radius: 0px;\n"
"    border-right: 0px solid rgb(255, 255, 255);\n"
"	border-top: 3px solid rgb(85, 123, 226);\n"
"	border-left: 0px solid rgb(85, 123, 226);\n"
"	border-bottom: 0px solid rgb(255, 255, 255);\n"
" }\n"
"\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 24, 2, 6)
        self.notifications_checkBox = QCheckBox(self.verticalGroupBox)
        self.notifications_checkBox.setObjectName(u"notifications_checkBox")
        self.notifications_checkBox.setMaximumSize(QSize(360, 16777215))
        self.notifications_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}\n"
"\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_10.addWidget(self.notifications_checkBox)

        self.soun_end_download_checkBox = QCheckBox(self.verticalGroupBox)
        self.soun_end_download_checkBox.setObjectName(u"soun_end_download_checkBox")
        self.soun_end_download_checkBox.setMaximumSize(QSize(360, 16777215))
        self.soun_end_download_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_10.addWidget(self.soun_end_download_checkBox)

        self.infoBox_checkBox = QCheckBox(self.verticalGroupBox)
        self.infoBox_checkBox.setObjectName(u"infoBox_checkBox")
        self.infoBox_checkBox.setMaximumSize(QSize(360, 16777215))
        self.infoBox_checkBox.setStyleSheet(u"QCheckBox:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
" QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"	padding-bottom: 4px;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	left: 5px;\n"
"	top: 2px;\n"
" }")

        self.verticalLayout_10.addWidget(self.infoBox_checkBox)


        self.verticalLayout_8.addWidget(self.verticalGroupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(70, 0))
        self.spinBox.setMaximumSize(QSize(100, 16777215))
        self.spinBox.setMinimum(-99)

        self.verticalLayout_7.addWidget(self.spinBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(287, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(668, 200))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 71))
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 1)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.token_group_lineEdit = QLineEdit(self.widget_2)
        self.token_group_lineEdit.setObjectName(u"token_group_lineEdit")
        self.token_group_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Segoe UI\";\n"
"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	padding-bottom: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
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
        self.token_group_lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.token_group_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.token_group_lineEdit, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 1)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.token_lineEdit = QLineEdit(self.widget1)
        self.token_lineEdit.setObjectName(u"token_lineEdit")
        self.token_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Segoe UI\";\n"
"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	padding-bottom: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
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

        self.horizontalLayout.addWidget(self.token_lineEdit, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.widget1, 0, Qt.AlignmentFlag.AlignTop)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setMaximumSize(QSize(16777215, 71))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.id_group_lineEdit = QLineEdit(self.widget2)
        self.id_group_lineEdit.setObjectName(u"id_group_lineEdit")
        self.id_group_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Segoe UI\";\n"
"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	padding-bottom: 5px;\n"
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

        self.horizontalLayout_2.addWidget(self.id_group_lineEdit, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.widget2, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.save_setings = QPushButton(self.widget)
        self.save_setings.setObjectName(u"save_setings")
        self.save_setings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 10pt \"Segoe UI\";\n"
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

        self.horizontalLayout_5.addWidget(self.save_setings)

        self.clear_pole_pushButton = QPushButton(self.widget)
        self.clear_pole_pushButton.setObjectName(u"clear_pole_pushButton")
        self.clear_pole_pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 10pt \"Segoe UI\";\n"
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

        self.horizontalLayout_5.addWidget(self.clear_pole_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.retranslateUi(Dialog_settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_settings)
    # setupUi

    def retranslateUi(self, Dialog_settings):
        Dialog_settings.setWindowTitle(QCoreApplication.translate("Dialog_settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.auto_swap_tab_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0410\u0432\u0442\u043e \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043e\u043a\u043d\u0430", None))
        self.auto_swap_time_data_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0410\u0432\u0442\u043e \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0434\u0430\u0442\u044b \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.blur_token_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0417\u0430\u0431\u043b\u044e\u0440\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u043a\u0435\u043d\u0430", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("Dialog_settings", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.notifications_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0441\u043b\u0435 \u043e\u0442\u043b\u043e\u0436\u043a\u0438", None))
        self.soun_end_download_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0417\u0432\u0443\u043a \u043f\u043e\u0441\u043b\u0435 \u0441\u043a\u0430\u0447\u043a\u0438", None))
        self.infoBox_checkBox.setText(QCoreApplication.translate("Dialog_settings", u"\u0418\u043d\u0444\u043e\u0431\u043b\u043e\u043a \u043f\u043e\u0441\u043b\u0435 \u043e\u0442\u043b\u043e\u0436\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_settings", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043a \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog_settings", u"  \u0420\u0430\u0437\u043d\u044b\u0435 \u0442\u043e\u0433\u043b\u044b  ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_settings", u"Group token", None))
        self.token_group_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_settings", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u043e\u0442 \u0441\u0432\u043e\u0435\u0439 \u0433\u0440\u0443\u043f\u043f\u044b \u0432\u043a", None))
        self.label.setText(QCoreApplication.translate("Dialog_settings", u"Access token", None))
        self.token_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_settings", u"(\u041d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0432\u0432\u043e\u0434\u0438\u0442\u044c \u043f\u043e\u043a\u0430 \u043d\u0435\u0442 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u0430 \u043d\u0430 \u0442\u043e\u043a\u0435\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_settings", u"id \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.id_group_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_settings", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u0440\u0443\u043f\u043f\u044b ", None))
        self.save_setings.setText(QCoreApplication.translate("Dialog_settings", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.clear_pole_pushButton.setText(QCoreApplication.translate("Dialog_settings", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog_settings", u"   \u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438   ", None))
    # retranslateUi

