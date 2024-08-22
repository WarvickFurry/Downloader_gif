# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_category.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_category_add_form(object):
    def setupUi(self, category_add_form):
        if not category_add_form.objectName():
            category_add_form.setObjectName(u"category_add_form")
        category_add_form.resize(503, 52)
        category_add_form.setStyleSheet(u"background-color: rgb(39, 39, 42);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(category_add_form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(category_add_form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom: 3px;\n"
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

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(category_add_form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 12pt \"Segoe UI\";\n"
"\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/close_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(category_add_form)

        QMetaObject.connectSlotsByName(category_add_form)
    # setupUi

    def retranslateUi(self, category_add_form):
        category_add_form.setWindowTitle(QCoreApplication.translate("category_add_form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("category_add_form", u"\u0432\u0432\u0435\u0441\u0442\u0438 \u0442\u0435\u0433 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.pushButton_2.setText("")
    # retranslateUi

