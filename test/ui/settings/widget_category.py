# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_category.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import res_rc

class Ui_category_list_widget(object):
    def setupUi(self, category_list_widget):
        if not category_list_widget.objectName():
            category_list_widget.setObjectName(u"category_list_widget")
        category_list_widget.resize(561, 366)
        category_list_widget.setStyleSheet(u"background-color: rgb(39, 39, 42);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(category_list_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label = QLabel(category_list_widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(category_list_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.remove_widget = QPushButton(category_list_widget)
        self.remove_widget.setObjectName(u"remove_widget")
        self.remove_widget.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 3px solid rgb(85, 123, 226);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 123, 226, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 123, 226, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/close_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_widget.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.remove_widget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category_lineEdit = QLineEdit(category_list_widget)
        self.category_lineEdit.setObjectName(u"category_lineEdit")
        self.category_lineEdit.setMinimumSize(QSize(0, 0))
        self.category_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout.addWidget(self.category_lineEdit)

        self.type_set_comboBox = QComboBox(category_list_widget)
        self.type_set_comboBox.addItem("")
        self.type_set_comboBox.addItem("")
        self.type_set_comboBox.addItem("")
        self.type_set_comboBox.addItem("")
        self.type_set_comboBox.setObjectName(u"type_set_comboBox")
        self.type_set_comboBox.setMaximumSize(QSize(263, 16777215))
        self.type_set_comboBox.setStyleSheet(u" QComboBox QAbstractItemView {\n"
"	font: 10pt \"Segoe UI\";\n"
"	min-width: 600px;\n"
" }")

        self.horizontalLayout.addWidget(self.type_set_comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(category_list_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"\n"
"border: 0px solid rgb(0, 0, 0);")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 30, 0, 0)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"	border-radius: 6;\n"
"	border: 3px solid rgb(85, 123, 226);")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(category_list_widget)

        QMetaObject.connectSlotsByName(category_list_widget)
    # setupUi

    def retranslateUi(self, category_list_widget):
        category_list_widget.setWindowTitle(QCoreApplication.translate("category_list_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("category_list_widget", u"\u0422\u0435\u0433 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("category_list_widget", u"0", None))
        self.remove_widget.setText("")
        self.category_lineEdit.setPlaceholderText(QCoreApplication.translate("category_list_widget", u"\u0432\u0432\u0435\u0441\u0442\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.type_set_comboBox.setItemText(0, QCoreApplication.translate("category_list_widget", u"\u0434\u043e\u0431\u043e\u0432\u043b\u0435\u043d\u0435 \u0442\u0435\u0433\u043e\u0432 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438  \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.type_set_comboBox.setItemText(1, QCoreApplication.translate("category_list_widget", u"\u0434\u043e\u0431\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u043b\u044c\u043a\u043e  \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.type_set_comboBox.setItemText(2, QCoreApplication.translate("category_list_widget", u"\u0438\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u0438\u0441\u043a \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.type_set_comboBox.setItemText(3, QCoreApplication.translate("category_list_widget", u"\u0438\u0441\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0442\u0435\u0433\u0438 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 (\u043d\u0435 \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u043e\u0432\u043b\u044f\u0442\u0441\u044f \u0442\u0435\u0433\u0438 \u0438\u0437 \u0434\u0430\u043d\u043d\u043e\u0439 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438)", None))

        self.groupBox.setTitle(QCoreApplication.translate("category_list_widget", u"\u0422\u0435\u0433\u0438  \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
    # retranslateUi

