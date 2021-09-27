# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(693, 559)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_img_name = QLabel(Form)
        self.lbl_img_name.setObjectName(u"lbl_img_name")

        self.verticalLayout.addWidget(self.lbl_img_name)

        self.lbl_img = QLabel(Form)
        self.lbl_img.setObjectName(u"lbl_img")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_img.sizePolicy().hasHeightForWidth())
        self.lbl_img.setSizePolicy(sizePolicy)
        self.lbl_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_img)

        self.lbl_status_msg = QLabel(Form)
        self.lbl_status_msg.setObjectName(u"lbl_status_msg")
        self.lbl_status_msg.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.verticalLayout.addWidget(self.lbl_status_msg)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_label_D = QPushButton(self.groupBox)
        self.btn_label_D.setObjectName(u"btn_label_D")
        self.btn_label_D.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color : rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color : rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_label_D.setCheckable(False)
        self.btn_label_D.setChecked(False)
        self.btn_label_D.setAutoDefault(False)
        self.btn_label_D.setFlat(False)

        self.gridLayout.addWidget(self.btn_label_D, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1, Qt.AlignHCenter)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1, Qt.AlignHCenter)

        self.btn_label_A = QPushButton(self.groupBox)
        self.btn_label_A.setObjectName(u"btn_label_A")
        self.btn_label_A.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color : rgb(62, 62, 62);\n"
"	background-color: rgb(255, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color : rgb(62, 62, 62);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_label_A.setCheckable(False)
        self.btn_label_A.setChecked(False)
        self.btn_label_A.setFlat(False)

        self.gridLayout.addWidget(self.btn_label_A, 2, 0, 1, 1)

        self.btn_label_S = QPushButton(self.groupBox)
        self.btn_label_S.setObjectName(u"btn_label_S")
        self.btn_label_S.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color : rgb(0, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color : rgb(0, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_label_S.setCheckable(False)
        self.btn_label_S.setChecked(False)
        self.btn_label_S.setFlat(False)

        self.gridLayout.addWidget(self.btn_label_S, 2, 1, 1, 1)

        self.btn_edit_classS = QPushButton(self.groupBox)
        self.btn_edit_classS.setObjectName(u"btn_edit_classS")

        self.gridLayout.addWidget(self.btn_edit_classS, 3, 1, 1, 1)

        self.btn_edit_classA = QPushButton(self.groupBox)
        self.btn_edit_classA.setObjectName(u"btn_edit_classA")

        self.gridLayout.addWidget(self.btn_edit_classA, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lbl_output_file = QLineEdit(Form)
        self.lbl_output_file.setObjectName(u"lbl_output_file")
        self.lbl_output_file.setEnabled(False)
        self.lbl_output_file.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lbl_output_file, 1, 1, 1, 1)

        self.btn_img_folder = QPushButton(Form)
        self.btn_img_folder.setObjectName(u"btn_img_folder")

        self.gridLayout_2.addWidget(self.btn_img_folder, 0, 3, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.btn_output_file = QPushButton(Form)
        self.btn_output_file.setObjectName(u"btn_output_file")

        self.gridLayout_2.addWidget(self.btn_output_file, 1, 3, 1, 1)

        self.lbl_image_folder = QLineEdit(Form)
        self.lbl_image_folder.setObjectName(u"lbl_image_folder")
        self.lbl_image_folder.setEnabled(False)
        self.lbl_image_folder.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lbl_image_folder, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tbl_browser = QTableWidget(self.groupBox_2)
        if (self.tbl_browser.columnCount() < 2):
            self.tbl_browser.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_browser.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_browser.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_browser.setObjectName(u"tbl_browser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tbl_browser.sizePolicy().hasHeightForWidth())
        self.tbl_browser.setSizePolicy(sizePolicy1)
        self.tbl_browser.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_browser.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_browser.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_browser.horizontalHeader().setVisible(True)

        self.verticalLayout_3.addWidget(self.tbl_browser)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        self.btn_label_D.setDefault(False)
        self.btn_label_A.setDefault(False)
        self.btn_label_S.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_img_name.setText(QCoreApplication.translate("Form", u"Image", None))
        self.lbl_img.setText("")
        self.lbl_status_msg.setText(QCoreApplication.translate("Form", u"Status Message", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Keyboard Controls", None))
        self.btn_label_D.setText(QCoreApplication.translate("Form", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"D", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"A", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"S", None))
        self.btn_label_A.setText(QCoreApplication.translate("Form", u"Customer", None))
        self.btn_label_S.setText(QCoreApplication.translate("Form", u"Staff", None))
        self.btn_edit_classS.setText(QCoreApplication.translate("Form", u"Edit class name", None))
        self.btn_edit_classA.setText(QCoreApplication.translate("Form", u"Edit class name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image Folder", None))
        self.btn_img_folder.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Output File", None))
        self.btn_output_file.setText(QCoreApplication.translate("Form", u"Load", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Labels", None))
        ___qtablewidgetitem = self.tbl_browser.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Image", None));
        ___qtablewidgetitem1 = self.tbl_browser.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Label", None));
    # retranslateUi

